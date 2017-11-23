# 2017-11-23

## tl;dr

   `mcflirt`, the motion-correction tool used in FSL `feat`, is
   instable to the one-voxel perturbation, for two reasons: (1) at the
   coarsest scale, the transformation estimated for volume /i/ is initialized
   from the transformation estimated for volume /i-1/; (2) the transformation
   estimated at scale /n/ is used to initialize the
   transformation at scale /n+1/. Fixing (1) is easy and it reduces
   instability. Fixing (2) is more complex, unless we completely get
   rid of the multi-scale approach, which would have other
   consequences.

## Stabilization

   Applied `mcflirt` from FSL 5.06 to the one-voxel and regular time
   series. Reference volume was 38, as for Niak. Obtained the
   following motion parameters:


  | Translation | Rotation |
  --------------|:---------|
  | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/translation.png) | ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/rotation.png) |

```
mcflirt -in ./sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel.nii.gz -out ./sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_mcflirt -mats -plots -rmsrel -rmsabs -spline_final
```

  The translation parameters are reasonably close to [the ones
  obtained with
  Niak](https://github.com/glatard/one-voxel/tree/master/stabilized-niak-motion-correction)
  but the rotation angles are slightly off, at least for the first
  volumes.

  The differences between motion parameters estimated on one-voxel and
  regular time-series are comparable to the differences [observed with Niak](https://github.com/glatard/one-voxel/tree/master/robust-motion):
  
  | Translation | Rotation |
  --------------|:---------|
  | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/differences-translation.png) | ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/differences-rotation.png) |

```
../scripts/diff_param_files.py ./onevoxel/sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_mcflirt.par ./regular/sub-01_ses-retest_task-overtwordrepetition_bold_mcflirt.par --mcflirt > difference.par
```

## Stabilization

An inspection of [`mcflirt`'s
code](https://github.com/mangstad/FSL/blob/fsl-5.0.9/src/mcflirt/mcflirt.cc)
reveals that motion correction is done through two nested iterative loops:
1. Four iterations are done with different scales (see `main` function). The
initial transformations at scale /n/ are the ones resulting from scale /n-1/, see for instance line 709 in the source code.
2. At each scale, transformations between volumes are estimated (see `correct` function). *At the first scaling level*, the transformation estimated on volume /i/ is used to initialize the transformation on volume /i+i/, see line 453.

The iterative initialization in 2. can be circumvented using flag
`-fudge` (undocumented). It reduces the instability to some extent:

  | Translation | Rotation |
  --------------|:---------|
  | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/fudge/differences-translations.png) | ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/fudge/differences-rotations.png) |

```
mcflirt -in ./sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel.nii.gz -out ./sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_mcflirt -mats -plots -rmsrel -rmsabs -spline_final -fudge
../scripts/diff_param_files.py ./onevoxel/sub-01_ses-retest_task-overtwordrepetition_bold_onevoxel_mcflirt.par ./regular/sub-01_ses-retest_task-overtwordrepetition_bold_mcflirt.par --mcflirt > difference.par
```

The remaining instability is most likely due to the iteration in 1. The current idea to stabilize it is to use a bootstrap technique.