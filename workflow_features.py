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

# for testing on one protein:
#s.set_results_dir()
#s.read_covariates()
#s.experiment = ('LCN15', '')
#s.protein = 'LCN15'
#s.ionmode = 'pos'
#s.peak_version = ''
#s.collect_peaks_files()
#s.set_sample_id_proc()
#s.set_ms2_param()
#s.one_experiment()

# generate profile plots with multiple thresholds
s = featureproc.Screen(
    'invitro',
    do_database_lookup = False,
    do_ms2 = False,
    do_export = False,
    explore_profile_filter = (5.0, 4.0, 3.0, 2.0, 1.5)
)
s.main()
