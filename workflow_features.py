#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright (c) 2019 - EMBL
#
#  File author(s): Dénes Türei (turei.denes@gmail.com)
#
#  This code is not for public use.
#  Please do not redistribute.
#  For permission please contact me.
#
#  Website: http://denes.omnipathdb.org/
#

import imp

from ltp import featureproc

s = featureproc.Screen('invitro')
s.main()



# generate profile plots with multiple thresholds
s = featureproc.Screen(
    'invitro',
    do_database_lookup = False,
    do_ms2 = False,
    do_export = False,
    explore_profile_filter = (5.0, 4.0, 3.0, 2.0, 1.5)
)
s.main()


# for testing on one protein:
s0 = featureproc.Screen('invitro')
s0.set_results_dir()
s0.read_covariates()
s0.experiment = ('GLTPD1', '')
s0.protein = 'GLTPD1'
s0.ionmode = 'pos'
s0.peak_version = ''
s0.exp_str = 'GLTPD1'
s0.collect_peaks_files()
s0.set_sample_id_proc()
s0.set_ms2_param()


s0.one_experiment()

# or step by step:
s0.setup_data()
s0.basic_filters()
s0.peak_size_filter(remove = False)
s0.samples.sort_all('mzs')
