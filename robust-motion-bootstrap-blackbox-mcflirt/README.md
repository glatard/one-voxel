# Results

![translation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/tx.png)
![translation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/ty.png)
![translation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/tz.png)
![rotation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/rx.png)
![rotation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/ry.png)
![rotation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/rz.png)

```
bootstrap-mcflirt.sh ./sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz
quick-plot-mcflirt.sh . one-voxel 100
plot_diff_iter_mcflirt.gnplt
```