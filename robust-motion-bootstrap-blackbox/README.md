# tl;dr

Implemented the Bootstrap on the complete motion correction chain, see
`scriptsmotion-correct.sh`. It is able to stabilize motion correction,
although the motion estimated for some volumes remains unstable.

# Results

Difference between the motion estimated from the initial time series and the time series after a one-voxel perturbation.

![translation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/tx.png)
![translation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/ty.png)
![translation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/tz.png)
![rotation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/rx.png)
![rotation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/ry.png)
![rotation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/rz.png)

```
motion-correct.sh ./sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz
quick-plot.sh . one-voxel 75
plot_diff_iter.gnplt
```