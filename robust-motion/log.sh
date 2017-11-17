../one_voxel.py ./sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz ./sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel.nii.gz
./motion-correct.sh sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel.nii.gz
./motion-correct.sh sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz

for file_name in sub-01_ses-retest_task-overtwordrepetition_bold_transf\
		     sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_transf
do
    for i in $(seq 0 75)
    do
	echo -n "$i, "
	./transfo_params.py ${file_name}_${i}_38.xfm
    done > ${file_name}_params.txt
done
