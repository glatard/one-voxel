# 2017-11-17

## tl;dr

  As observed
 [there](https://github.com/glatard/one-voxel/tree/master/verifyFiles)
 (see last animation), the one-voxel perturbation had an effect on
 motion correction.  Here we observe the one-voxel perturbation has no
 effect on rigid registration when executed independently from motion
 correction. In motion correction, the initialization of registration
 /n/ from the transformation resulting from registration /n-1/ creates
 instabilities. Registering the volumes independently from each other
 fixes instabilities.

## Implementation

I implemented a basic motion correction procedure in
  `motion-correct.sh`, to facilitate experimentation outside of the
  Niak environment. It applies `minctracc` iteratively on the volumes
  of the 4D sequence. The rigid transormation is initialized either
  (1) from the transformation resulting from the previous iteration
  (or the identity at iteration 0), or (2) from the
  identity. `minctract` is used with the following parameters which
  are roughly consistent with the ones used in Niak:

```
minctracc <source_vol> <target_vol> -clobber -xcorr -forward -lsq6 -speckle 0 -est_center -tol 0.0005 -trilinear -simplex 10 -model_lattice -step 10 10 10 <out_trsf> -transformation <init_transfo>`

```

## Validation

I tested `motion-correct.sh` on the same subject as
  [there](https://github.com/glatard/one-voxel/tree/master/verifyFiles),
  obtained the following motion parameters:

  | Translation | Rotation |
  --------------|:---------|
  | ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/sub-01_ses-retest_task-overtwordrepetition_bold_transf_params-0.png) | ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/sub-01_ses-retest_task-overtwordrepetition_bold_transf_params-1.png) |
  
  The motion parameters are consistent with the [ones produced by
  Niak](https://github.com/glatard/one-voxel/tree/master/verifyFiles). The
  differences are explained by the following limitations of
  `motion-correct.sh`: (1) it doesn't mask the brain, (2) `minctracc`
  may not use exactly the same parameters as in Niak, (3) the
  reference volume is `nvol/2` which may not be consistent with Niak,
  (4) in Niak, motion correction parameters are also estimated across
  runs (I didn't completely get that part). But overall
  `motion-correct.sh` is a good model of the motion correction done in
  Niak.

## Result

When the transformation at iteration /n/ is initialized from the result
  of iteration /n-1/, the following differences on the motion
  parameters are observed between the original sequence and the
  sequence with the one-voxel perturbation:

  | Translation | Rotation |
  --------------|:---------|
  | ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff-0.png) | ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff-1.png) |

The motion parameters are not stable. The effect of the one-voxel
perturbation propagates along the time series. The impact of the
perturbation on volumes of the time series is not uniform.

When the transformations are all initialized from the identity, the
differences become negligible:

  | Translation | Rotation |
  --------------|:---------|
  | ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff_idinit-0.png) | ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff_idinit-1.png) |


Conclusion: the recursive initialization is responsible for instabilities.

## Command log

See `log.sh`