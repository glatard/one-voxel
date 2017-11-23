#!/usr/bin/env bash

set -e
set -u

function run {
    ("$@" &> last_log.log && echo "[ OK ] $*") || ( echo "[ FAILED ] $*" ; cat last_log.log ; exit 1 )
}

if [ $# != 4 ]
then
    echo "usage: $0 <anat_image> <func_image> <anat_mask> <func_mask>"
    exit 1
fi

anat=$1
func=$2
anat_mask=$3
func_mask=$4

anat_masked="$(basename ${anat} .mnc)_masked.mnc"
func_masked="$(basename ${func} .mnc)_masked.mnc"

guess_tfm="guess.xfm"
temp_tfm="temp.xfm"
estimate_tfm="estimate.xfm"
anat_resampled="$(basename "${anat}" .mnc)_resampled.mnc"
anat_smoothed="$(basename "${anat}" .mnc)_smoothed"
func_smoothed="$(basename "${func}" .mnc)_smoothed"

# initialize guess
run param2xfm -clobber "${guess_tfm}" -translation 0 0 0 -rotations 0 0 0 -clobber

run mincmath -mult "${anat}" "${anat_mask}" "${anat_masked}"
run mincmath -mult "${func}" "${func_mask}" "${func_masked}"

c=0
for i in 8,4,8 3,4,4 8,4,2 4,2,2 3,1,1
do
    OLDIFS=${IFS}
    IFS=","
    set -- $i
    smooth=$1
    step=$2
    simplex=$3
    IFS=${OLDIFS}
    echo
    echo "> Iteration ${c}, smooth=${smooth}, step=${step}, simplex=${simplex}"
    # Note: in niak, resampling is done to tfm space (requires -dircos,etc)
    run mincresample "${anat_masked}" "${anat_resampled}" -clobber -transform "${guess_tfm}" -tricubic -like "${func_masked}"
    run mincblur -3dfwhm "${smooth}" "${smooth}" "${smooth}" -no_apodize -clobber "${anat_resampled}" "${anat_smoothed}"
    run mincblur -3dfwhm "${smooth}" "${smooth}" "${smooth}" -no_apodize -clobber "${func_masked}" "${func_smoothed}"
    run minctracc "${anat_smoothed}.mnc_blur.mnc" "${func_smoothed}.mnc_blur.mnc" "${estimate_tfm}" -mi -threshold -50 -1248 -identity -simplex "${simplex}" -tol 0.00005 -step "${step}" "${step}" "${step}" -lsq6 -clobber
    run xfmconcat "${guess_tfm}" "${estimate_tfm}" "${temp_tfm}"
    run mv -f "${temp_tfm}" "${guess_tfm}"
    run cp ${guess_tfm} ${c}_${guess_tfm}
    c=$(( c + 1 ))
done

#Resample one last time
run mincresample "${anat}" "${anat_resampled}" -clobber -transform "${guess_tfm}" -tricubic -like "${func_masked}"
