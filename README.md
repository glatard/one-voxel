# Niak one-voxel

A one-voxel experiment with the Niak pre-processing pipeline.

## 2017-11-14

* Fixed error with Niak pre-processing in CBRAIN. The dataset had an extra level of directories that prevented Niak from finding `dataset_description.json`.
* Used BIDS dataset `ds114` instead of `ds001` because `ds001` has no information about slice timing.
* Reviewed the parameters of the Niak pre-processing pipelines and decided to use the default values :)

## 2017-10-31

* Created `one-voxel.py` to change the intensity of the central voxels of all the volumes in an image sequence by 1%.