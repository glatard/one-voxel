fslroi sub-01_ses-test_task-linebisection_bold.nii.gz vol0.nii.gz 0 1 
fslroi sub-01_ses-test_task-linebisection_bold.nii.gz vol1.nii.gz 1 1 
minctracc vol0.nii.gz vol1.nii.gz -xcorr -forward -lsq6 -speckle 0  -est_center -simplex 10 transfo.xfm
../one_voxel.py vol0.nii.gz vol0-onevoxel.nii.gz
../one_voxel.py vol1.nii.gz vol1-onevoxel.nii.gz
minctracc vol0.nii.gz vol1-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0  -est_center -simplex 10 transfo-1.xfm
minctracc vol0-onevoxel.nii.gz vol1.nii.gz -xcorr -forward -lsq6 -speckle 0  -est_center -simplex 10 transfo-2.xfm
minctracc vol0-onevoxel.nii.gz vol1-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0  -est_center -simplex 10 transfo-3.xfm

# With vol0 and vol124
fslroi sub-01_ses-test_task-linebisection_bold.nii.gz vol124.nii.gz 123 1
minctracc vol0.nii.gz vol124.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-4.xfm
minctracc vol0.nii.gz vol124-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-5.xfm
minctracc vol0-onevoxel.nii.gz vol124.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-6.xfm
minctracc vol0-onevoxel.nii.gz vol124-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-7.xfm
  #-> very small difference, only on t_x

# With vol 6
fslroi sub-01_ses-test_task-linebisection_bold.nii.gz vol6.nii.gz 6 1
minctracc vol6.nii.gz vol124.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-0-124-0.xfm
minctracc vol6.nii.gz vol124-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-0-124-1.xfm
minctracc vol6-onevoxel.nii.gz vol124.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-0-124-2.xfm
minctracc vol6-onevoxel.nii.gz vol124-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-0-124-3.xfm

# With vol 6 - sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz
\rm -f vol*.nii.gz
\rm -f transfo*.xfm
fslroi sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz vol6.nii.gz 6 1
fslroi sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz vol34.nii.gz 34 1
../one_voxel.py vol6.nii.gz vol6-onevoxel.nii.gz
../one_voxel.py vol34.nii.gz vol34-onevoxel.nii.gz

minctracc vol6.nii.gz vol34.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-0.xfm
minctracc vol6.nii.gz vol34-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-1.xfm
minctracc vol6-onevoxel.nii.gz vol34.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-2.xfm
minctracc vol6-onevoxel.nii.gz vol34-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-3.xfm

# With vol 8 - sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz
\rm -f vol*.nii.gz
\rm -f transfo*.xfm
fslroi sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz vol8.nii.gz 8 1
fslroi sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz vol34.nii.gz 34 1
../one_voxel.py vol8.nii.gz vol8-onevoxel.nii.gz
../one_voxel.py vol34.nii.gz vol34-onevoxel.nii.gz

minctracc vol8.nii.gz vol34.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-4.xfm
minctracc vol8.nii.gz vol34-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-5.xfm
minctracc vol8-onevoxel.nii.gz vol34.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-6.xfm
minctracc vol8-onevoxel.nii.gz vol34-onevoxel.nii.gz -xcorr -forward -lsq6 -speckle 0 -est_center -simplex 10 transfo-7.xfm
