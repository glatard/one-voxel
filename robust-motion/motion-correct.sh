#!/usr/bin/env bash

set -e
set -u

function run {
    $quiet || echo $*
    $* &> last_log.log
    if (( $? != 0 ))
    then
	cat last_log.log
	exit 1
    fi
}

if [ $# != 1 ]
then
    echo "usage: $0 <func_image_nii>"
    echo "     func_imagee_nii: a 4D .nii.gz image"
    exit 1
fi

quiet=false
minctrac_opts="-clobber -xcorr -forward -lsq6 -speckle 0 -est_center -tol 0.0005  -trilinear -simplex 10 -model_lattice -step 10 10 10"
# TODO: compute brain masks and use them for minctracc

# has to be a .nii.gz image
func_image_nii=$1

# convert to mnc

func_name=$(echo ${func_image_nii} | awk -F '.nii.gz' '{print $1}')
func_image_mnc="${func_name}.mnc"
run nii2mnc -clobber ${func_image_nii} ${func_image_mnc}

n_vols=$(mincinfo -dimlength time ${func_image_mnc})
last_vol=$((${n_vols}-1))
n_ref_vol=$((${n_vols}/2))

# extract volumes
for i in $(seq 0 ${last_vol})
do
    run mincreshape -clobber -dimrange time=${i} ${func_image_mnc} ${func_name}_vol_${i}.mnc
done

run param2xfm -clobber identity.xfm -translation 0 0 0 -rotations 0 0 0 -clobber

# motion correction
for i in $(seq 0 ${last_vol})
do
    if (( $i == 0 ))
    then
	init_transfo="identity.xfm"
    else
	i_prev=$(($i-1))
	init_transfo=transf_${i_prev}_${n_ref_vol}.xfm
    fi
    run minctracc ${func_name}_vol_${i}.mnc ${func_name}_vol_${n_ref_vol}.mnc ${minctrac_opts} ${func_name}_transf_${i}_${n_ref_vol}.xfm -transformation ${init_transfo}
done


