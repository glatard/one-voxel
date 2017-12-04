

# Estimated parameters

| Niak / minctools | FSL / mcflirt |
-------------------|:--------------|
| ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/sub-01_ses-retest_task-overtwordrepetition_bold_transf_params-0.png) | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/translation.png)|
| ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/sub-01_ses-retest_task-overtwordrepetition_bold_transf_params-1.png) | ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/rotation.png) |

# Stability

Stability is measured as the difference between the motion estimated from the initial time series and the time series after a one-voxel perturbation.

## Initial

| Niak / minctools | FSL / mcflirt |
-------------------|:--------------|
| ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff-0.png) | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/differences-translation.png) |
| ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff-1.png) |   ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/differences-rotation.png) |

## Independent initialization

Transformation between volume i and volume i+1 is initialized from the identity matrix rather than from transformation between volume i-1 and i.

| Niak / minctools | FSL / mcflirt |
-------------------|:--------------|
| ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff_idinit-0.png) | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/fudge/differences-translations.png) |
| ![alt text](https://github.com/glatard/one-voxel/raw/master/robust-motion/diff_idinit-1.png) | ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/fudge/differences-rotations.png) |

## Bootstrap

Convergence of the bootstrap estimate, from 1 to 100 iterations.

| Niak / minctools | FSL / mcflirt |
-------------------|:--------------|
| ![translation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/tx.png) | ![translation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/tx.png) |
| ![translation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/ty.png) | ![translation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/ty.png) |
| ![translation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/tz.png) | ![translation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/tz.png) |
| ![rotation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/rx.png) | ![rotation_x](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/rx.png) |
| ![rotation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/ry.png) | ![rotation_y](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/ry.png) |
![rotation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox/rz.png) | ![rotation_z](https://github.com/glatard/one-voxel/raw/master/robust-motion-bootstrap-blackbox-mcflirt/rz.png) |
