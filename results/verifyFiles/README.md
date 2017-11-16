# Command line

`verifyFiles.py ./conditions.txt onevoxel -m ./metrics.txt -e ./exclusions.txt`

# Results

* checksum comparisons: `onevoxel_differences_subject_total.txt`. Nothing special to report, the only identical files are the obvious ones (css, html, js files and others)

* compared the normalized mean-square error of nifti files using [nrmse.sh](https://github.com/big-data-lab-team/repro-tools/blob/master/metrics/nrmse.sh): `nrmse.csv`

* `anat_sub0{1,2}_nativefunc_hires.nii.gz` don't have the same dimensions in `regular` and `onevoxel`:
     ```
     $ fslinfo onevoxel/ds114-small/anat/sub01/anat_sub01_nativefunc_hires.nii.gz 
       data_type      FLOAT64
       dim1           182
       dim2           259
       dim3           217
     ```
     ```
     $ fslinfo regular/ds114-small/anat/sub01/anat_sub01_nativefunc_hires.nii.gz 
       data_type      FLOAT64
       dim1           182
       dim2           260
       dim3           218
     ```

* compared `func/sub01/fmri_sub01_sesstest_taskrest.nii.gz`:

![alt text](https://github.com/glatard/one-voxel/raw/master/results/fmri_sub01_sesstest_taskrest.gif)

* compared `anat/sub01/anat_sub01_nuc_stereonl.nii.gz`

![alt text](https://github.com/glatard/one-voxel/raw/master/results/anat_sub01_nuc_stereonl.gif)

* compared `anat/sub01/anat_sub01_classify_stereolin.nii.gz`

![alt text](https://github.com/glatard/one-voxel/raw/master/results/comp_anat_sub01_classify_stereolin.gif)

```
fslview onevoxel/ds114-small/anat/sub01/anat_sub01_classify_stereolin.nii.gz # take screenshot in 1.png
fslview regular/ds114-small/anat/sub01/anat_sub01_classify_stereolin.nii.gz # take screenshot in 2.png
convert -loop 0 1.png 2.png comp.gif
convert comp.gif -coalesce -repage 0x0 -crop 614x660+478+927 +repage comp_anat_sub01_classify_stereolin.gif
```

* computed correlations between time series using Niak's `niak_test_cmp_files` (see `compare_4D.m`):

```
""  "max_corr"  "min_corr"  "mean_corr"
"ds114-small/fmri/fmri_sub01_sessretest_taskrest.nii.gz"  0.999990820884705  -0.728667438030243  0.976761400699615
"ds114-small/fmri/fmri_sub01_sesstest_taskrest.nii.gz"  0.999991118907928  -0.848057329654694  0.945828080177307
"ds114-small/fmri/fmri_sub02_sessretest_taskrest.nii.gz"  0.999993920326233  -0.906261980533600  0.895831763744354
"ds114-small/fmri/fmri_sub02_sesstest_taskrest.nii.gz"  0.999995648860931  -0.929119884967804  0.957925915718079
"ds114-small/resample/fmri_sub01_sessretest_taskrest_n.nii.gz"  0.999999642372131  -0.238747075200081  0.991999864578247
"ds114-small/resample/fmri_sub01_sesstest_taskrest_n.nii.gz"  0.999999880790710  -0.712236404418945  0.991920232772827
"ds114-small/resample/fmri_sub02_sessretest_taskrest_n.nii.gz"  0.999980151653290  -0.746837317943573  0.964701175689697
"ds114-small/resample/fmri_sub02_sesstest_taskrest_n.nii.gz"  0.999953866004944  -0.462472826242447  0.972331345081329
```

```awk -F ',' '$NF!="NaN" {print $1" "$(NF-2)" "$(NF-1)" "$NF}' compare.csv```

What happens between 'resample' and 'fmri' is the regression of confounds. @pbellec said the correlation should be plotted after having removed the scrubbed volumes.

* motion-correction plots, before and after perturbation:

![alt text](https://github.com/glatard/one-voxel/raw/master/results/comp_motion_report.gif)

