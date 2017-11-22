# Niak one-voxel

A one-voxel experiment with the Niak pre-processing pipeline.

## Log

### 2017-11-20

* What makes small variations small? They are considered small when
  compared to other, canonical, variations. For instance, the
  one-voxel variation is considered small because the variability
  coming from acquisition noise is much more important. 

* About the definition of stability: a pipeline is an application p: X
-> Y. There are distances dX and dY defined on X and Y. When a
perturbation x is applied to x0 in X, we define y(x, x0) = dY(p(x0+x),
p(x0)). p is usually not linear, even when linear transforms such as
rigid registration are mainly involved in p (think: is the result of
rigid transformation linearly related to the initialization of the
optimization process).

* L'objectif de cette definition de la stabilite est de s'affranchir
  d'une reference quantitative dependante de chaque etape du
  pipeline. Nous cherchons une definition de la stabilite qui
  ne dependrait pas d'un seuil propre a chaque application. 

Soit f la fonction de x, x0 telle que dY(p(x0+x), p(x0)) = f(  dX(x+x0, x0) ).
La stabilite en x0 est definie a partir de df/dx(x0)

Instabilite nulle: df/dx = 0
Instabilite lineaire: df/dx = k
Instabilite quadratique: df/dx = kx
...

La definition de la distance est indeniablement dependante de l'application.

### 2017-11-17

* The instability comes from the initialization of registration /n/
  from the transformation resulting from registration /n-1/ in the
  time series. Registering the volumes independently from each other
  fixes the instability. See details
  [here](https://github.com/glatard/one-voxel/tree/master/robust-motion).

### 2017-11-16

* Didn't manage to reproduce variability in the transformations
  produced by `minctrac` between 2 volumes of
  `sub-01_ses-retest_task-overtwordrepetition_bold.nii.gz` in
  `ds114`. Most likely, this is because *rigid registration is not
  unstable, motion correction is*. If this is true, feat and
  [fmriprep](http://fmriprep.readthedocs.io/en/stable/workflows.html)
  should both be impacted by the same problem since they use
  [mcflirt](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/MCFLIRT) which also
  initializes n from n-1. But SPM doesn't seem to be doing that
  (spm_realign). Unclear if AFNI's
  [3dvolreg](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dvolreg.html),
  used by C-PAC, does that.

* Started a script to average rigid transformations, to be used to bootstrap rigid registration (`robust-motion/average_transfo.py`). Based on the framework in [there](https://link.springer.com/chapter/10.1007%2F11866763_19?LI=true).

* Priority  list following the [first results](https://github.com/glatard/one-voxel/tree/master/results/verifyFiles):

- [ ] Bootstrap rigid registration
- [ ] Test on more subjects
- [ ] Test with feat, SPM, fmriprep
- [ ] Comparison with effect of the OS
- [ ] Define a proper stability measure

### 2017-11-15

* Following Slack thread with @pbellec: the instability of motion estimation needs to be fixed; it could be fixed by averaging registrations. 

* It would be interesting to compare the one-voxel effect to the effect of the OS.

* We need a better distance than just the NRMSE to compare images, as
  it is too global. Visually, we often are interested in local
  measures. We could use the max distance (e.g., NRMSE) between blocks
  of size, say 1/10 of the image. 

* To compare the effect of the perturbation on file A and
  file B of the pipeline, we should normalize whatever distance is
  applied to file A by its standard deviation computed /on all the
  subjects/. The normalized distance of file A could then be compared
  to the normalized distance on file B. See how this relates to the
  Mahanalobis norm.

* Read https://en.wikipedia.org/wiki/Numerical_stability and
  references. Very instructive.

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
