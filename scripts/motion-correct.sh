#!/usr/bin/env bash

set -e
set -u

function run {
    local log_file="last_log_motion_correct.log"
    local complete_log="log_motion_correct.log"
    (start=$(date +%s%N); "$@" &> ${log_file} && stop=$(date +%s%N) && time=$(echo "scale=4 ; $(((stop-start))) / 1000000000.0" | bc) && echo "[ OK ] (${time}s) $*") || ( echo "[ FAILED ] $*" ; cat ${log_file} ; exit 1 )
    cat ${log_file} >> ${complete_log}
}

if [ $# != 1 ]
then
    echo "usage: $0 <func_image_nii>"
    echo "     func_imagee_nii: a 4D .nii.gz image"
    exit 1
fi

minctrac_opts="-clobber -xcorr -forward -lsq6 -speckle 0 -est_center -tol 0.0005  -trilinear -simplex 10 -model_lattice -step 10 10 10"

# Creates identity transformation
run param2xfm -clobber identity.xfm -translation 0 0 0 -rotations 0 0 0 -clobber

# bootstrap
n_samples=100
for n in $(seq 1 ${n_samples})
do
    echo
    echo "> Iteration ${n}"

    # Add noise to functional image
    func_image_nii=$1
    func_name=$(echo ${func_image_nii} | awk -F '.nii.gz' '{print $1}')
    temp_func_image_nii=${func_name}_${n}.nii.gz # will contain the noise
    run one_voxel.py --random ${func_image_nii} ${temp_func_image_nii}
    func_image_nii=${temp_func_image_nii}
    
    # Convert to mnc
    func_name=$(echo ${func_image_nii} | awk -F '.nii.gz' '{print $1}')
    func_image_mnc="${func_name}.mnc"
    test -f ${func_image_mnc} || ((test -f ${func_name}.nii || run gunzip ${func_image_nii}) && run nii2mnc ${func_name}.nii ${func_image_mnc})

    # Get reference volume
    n_vols=$(mincinfo -dimlength time ${func_image_mnc})
    last_vol=$((${n_vols}-1))
    n_ref_vol=$((${n_vols}/2))

    # Extract volumes
    for i in $(seq 0 ${last_vol})
    do
	test -f ${func_name}_vol_${i}.mnc || run mincreshape -clobber -dimrange time=${i} ${func_image_mnc} ${func_name}_vol_${i}.mnc
    done
    
    # Motion correction 
    for i in $(seq 0 ${last_vol})
    do
	if (( $i == 0 ))
	then
	    init_transfo="identity.xfm"
	else
	    init_transfo=${output_transfo} # output from previous iteration
	fi
	output_transfo=${func_name}_transf_${i}_${n_ref_vol}_bootstrap.${n}.xfm
	
	# init from i-1 -- bootstrap
	run minctracc ${func_name}_vol_${i}.mnc ${func_name}_vol_${n_ref_vol}.mnc ${output_transfo} -transformation ${init_transfo} ${minctrac_opts} 
	# init from identity -- bootstrap
	# run minctracc ${func_name}_vol_${i}.mnc ${func_name}_vol_${n_ref_vol}.mnc ${output_transfo} -transformation identity.xfm ${minctrac_opts}
    
    done
    
    # Compute the sample averages, for each volume
    # This is used to plot the evolution of the average by iteration
    func_image_nii=$1
    func_name=$(echo ${func_image_nii} | awk -F '.nii.gz' '{print $1}')
    for i in $(seq 0 ${last_vol})
    do
	transfos=""
	for k in $(seq 1 ${n})
	do
	    transfo=${func_name}_${k}_transf_${i}_${n_ref_vol}_bootstrap.${k}.xfm
	    transfos="${transfos} ${transfo}"
	done
	output_transfo=${func_name}_transf_${i}_${n_ref_vol}_bootstrap_iter_${n}.xfm
	run transfo_stats.py ${transfos} ${output_transfo} 
    done
done

# Compute the final averages
func_image_nii=$1
func_name=$(echo ${func_image_nii} | awk -F '.nii.gz' '{print $1}')
for i in $(seq 0 ${last_vol})
do
    transfos=""
    for n in $(seq 1 ${n_samples})
    do
	transfo=${func_name}_${n}_transf_${i}_${n_ref_vol}_bootstrap.${n}.xfm
	transfos="${transfos} ${transfo}"
    done
    output_transfo=${func_name}_transf_${i}_${n_ref_vol}_bootstrap.xfm
    run transfo_stats.py ${transfos} ${output_transfo} 
done
