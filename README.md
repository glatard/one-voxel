# Niak one-voxel

A one-voxel experiment with the Niak pre-processing pipeline.

## Tools

* `one-voxel.py`: changes the intensity of the central voxels of all
  the volumes in an image sequence by 1%.

## Log

### 2017-11-14

* Differences between `regular` and `onevoxel`: see `results/verifyfiles`

* Pipeline results

  | ds114-small | ds114-small-onevoxel |
  --------------|:--------------------:|
  | results-directory-471071-783976569.niak | results-directory-471077-897624584.niak |


* Relaunched the two tasks on `AceLab-Docker-1` (471077 and 471071)
  because tasks have been queuing for several hours on Graham. It
  seems that pre-processing tasks are still started with a walltime of
  3 days, which makes them queued forever. Tasks completed
  successfully. Leaving the two task on Graham running to make sure
  that results are identical.
* Started looking into `niak_test_all.m` to see how pre-processing
  results are compared to "a reference version of the
  results". Comparisons are in `niak_brick_cmp_files.m`.
* Launched pre-processing of `ds114-small` and `ds114-small-onevoxel`
  on CBRAIN (tasks #471072 and #471075), Graham cluster. Small
  datasets only have two subjects. It looks like Niak will pre-process
  the two sessions in each subject. 
* Fixed error with Niak pre-processing in CBRAIN. The dataset had an
  extra level of directories that prevented Niak from finding
  `dataset_description.json`.
* Used BIDS dataset `ds114` instead of `ds001` because `ds001` has no
  information about slice timing.
* Reviewed the parameters of the Niak pre-processing pipelines and
  decided to use the default values except for "Slice timing type
  scanner".

### 2017-10-31

* Created `one-voxel.py` to change the intensity of the central voxels
  of all the volumes in an image sequence by 1%.