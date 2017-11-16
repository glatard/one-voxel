% Adapted from /usr/local/niak/extensions/niak_test/niak_test_fmripreproc_demoniak.m

in_c.source = {};
in_c.target = {};

folder_1 = 'onevoxel' % change this to the first results folder
folder_2 = 'regular' % change this to the second results folder
out_c = ['./test.csv']; % output file

opt_c.base_source = folder_1;
opt_c.base_target = folder_2;
opt_c.black_list_source{1} = [folder_1 'logs' filesep];
opt_c.black_list_target{1} = [folder_2 'logs' filesep];
opt_c.black_list_source{2} = [folder_1 'pipe_parameters.mat' ];
opt_c.black_list_target{2} = [folder_2 'pipe_parameters.mat' ];
niak_test_cmp_files(in_c, out_c, opt_c, false)

