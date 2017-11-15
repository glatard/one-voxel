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
* compared `anat/sub01/anat_sub01_classify_stereolin.nii.gz`

![alt text](https://github.com/glatard/one-voxel/raw/master/results/comp_anat_sub01_classify_stereolin.gif)

```
fslview onevoxel/ds114-small/anat/sub01/anat_sub01_classify_stereolin.nii.gz # take screenshot in 1.png
fslview regular/ds114-small/anat/sub01/anat_sub01_classify_stereolin.nii.gz # take screenshot in 2.png
convert -loop 0 1.png 2.png comp.gif
convert comp.gif -coalesce -repage 0x0 -crop 614x660+478+927 +repage comp_anat_sub01_classify_stereolin.gif
```