#!/usr/bin/env bash

set -e
set -u

if [ $# != 4 ]
then
    echo "usage: $0 <dir1> <dir2> <min_iter> <max_iter>"
    echo "Compares the transformations obtained for a number of iteration comprised between <min_iter> and <max_iter>. Puts the differences in diff_iter_<i>.txt where <i> is the number of iterations."
    exit 1
fi

DIR1=$1
DIR2=$2
A=$3
B=$4

for iter in $(seq ${A} ${B})
do
    diff_param_files.py ${DIR1}/sub-01_ses-retest_task-overtwordrepetition_bold_${iter}_mcflirt_iter_${iter}.par ${DIR2}/sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_${iter}_mcflirt_iter_${iter}.par  > diff_iter_${iter}.txt --mcflirt
done
