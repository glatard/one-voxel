# Do one-voxel perturbation
../one_voxel.py ./sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz ./sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel.nii.gz

# Do motion correction
# regular
./motion-correct.sh sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz
# onevoxel
./motion-correct.sh sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel.nii.gz

# Print transform param files
for file_name in sub-01_ses-retest_task-overtwordrepetition_bold_transf\
		     sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_transf
do
    for i in $(seq 0 75)
    do
	echo -n "$i, "
	./transfo_params.py ${file_name}_${i}_38.xfm
    done > ${file_name}_params.txt
done

# Diff transform param files
./diff_param_files.py sub-01_ses-retest_task-overtwordrepetition_bold_transf_params.txt sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_transf_params.txt > diff.txt

### ID INIT

# Print transform param files (id init)
for file_name in sub-01_ses-retest_task-overtwordrepetition_bold_transf\
		     sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_transf
do
    for i in $(seq 0 75)
    do
	echo -n "$i, "
	./transfo_params.py ${file_name}_${i}_38_idinit.xfm
    done > ${file_name}_params_idinit.txt
done

# Diff transform param files (id init)
./diff_param_files.py sub-01_ses-retest_task-overtwordrepetition_bold_transf_params_idinit.txt sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_transf_params_idinit.txt > diff_idinit.txt

# Plot results
./plot_params.gnplt
