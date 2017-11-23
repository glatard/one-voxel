# 2017-11-23

## tl;dr

   `mcflirt`, the motion-correction tool used in FSL `feat` is
   instable to the one-voxel perturbation, for two reasons: (1) at the
   coarsest scale, the transformation to volume /i/ is initialized
   from the transformation to volume /i-1/; (2) the transformation
   obtained at smoothing scale /n/ is used to initialize the
   transformation at scale /n+1/. Fixing (1) is easy and it reduces
   instability. Fixing (2) is more complex, unless we completely get
   rid of the multi-scale approache, which would have other
   consequences.

## There are instabilities

   Applied `mcflirt` from FSL 5.06 to the one-voxel and regular time
   series. Reference volume was 38, as for Niak. Obtained the
   following motion parameters:


  | Translation | Rotation |
  --------------|:---------|
  | ![translation](https://github.com/glatard/one-voxel/raw/master/mcflirt/translation.png) | ![rotation](https://github.com/glatard/one-voxel/raw/master/mcflirt/rotation.png) |

  The translation parameters are reasonably close to [the ones
  obtained with
  Niak](https://github.com/glatard/one-voxel/tree/master/stabilized-niak-motion-correction)
  but the rotation angles are slightly off.

  The differences between motion parameters estimated from one-voxel
   