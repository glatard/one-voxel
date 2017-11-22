# 2017-11-22

## Method

Fixed Niak's motion parameter estimation so that it doesn't initialize
the transformation related to volume /i/ with the transformation
related to volume /i-i/. See [Git
commit](https://github.com/glatard/niak/commit/e2e7dd1c84ffd580068892183c2d94d340825d73). This is based on [these
observations](https://github.com/glatard/one-voxel/tree/master/robust-motion).

## Result

* Before the fix (one-voxel vs regular):

![alt text](https://github.com/glatard/one-voxel/raw/master/stabilized-niak-motion-correction/screenshots/iterative_cropped.gif)

`convert -loop 0 onevoxel-iterative.png regular-iterative.png iterative.gif`

`convert iterative.gif -coalesce -repage 0x0 -crop 3200x1500+0+1400
+repage iterative_cropped.gif`

* After the fix (one-voxel vs regular):

![alt text](https://github.com/glatard/one-voxel/raw/master/stabilized-niak-motion-correction/screenshots/stabilized_cropped.gif)

## Conclusion

* The estimated motion parameters are now identical for the one-voxel
  and the regular time series, problem solved!

* There are still differences in the image overlays (right column),
  most likely due to non-linear registration.

* Stability cannot be the only criterion, accuracy also has to be measured. 