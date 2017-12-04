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

# bootstrap
n_samples=100
param_files=""

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
    func_name=$(echo ${func_image_nii} | awk -F '.nii.gz' '{print $1}')

    run mcflirt -in ${func_image_nii} -out ${func_name}_mcflirt -mats -plots -rmsrel -rmsabs -spline_final
    param_files="${param_files} ${func_name}_mcflirt.par"
    
    # Compute the sample averages, for each volume
    # This is used to plot the evolution of the average by iteration
    output_params=${func_name}_mcflirt_iter_${n}.par
    run average_param_files.py ${param_files} ${output_params}
done
