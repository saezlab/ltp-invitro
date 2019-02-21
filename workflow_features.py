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

import os
import shutil
import imp

from ltp import featureproc
from lipyd import ms2
from lipyd import sample
from lipyd import feature
from lipyd import lipproc

def reload():
    
    imp.reload(lipproc)
    imp.reload(ms2)
    imp.reload(sample)
    imp.reload(feature)
    imp.reload(featureproc)

s = featureproc.Screen('invitro')
s.main()

# to use different peak ratio threshold:
s = featureproc.Screen(
    'invitro',
    profile_filter_args = {'tolerance': 1.5}
)
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
s0.experiment = ('STARD10', '')
s0.protein = 'STARD10'
s0.ionmode = 'pos'
s0.peak_version = ''
s0.exp_str = 'STARD10'
s0.collect_peaks_files()
s0.set_sample_id_proc()
s0.set_ms2_param()


s0.one_experiment()

# or step by step:
s0.setup_data()
s0.basic_filters()
s0.peak_size_filter(remove = False)
s0.samples.sort_all('mzs')


# checking multiple ratios for RLBP1:
s0 = featureproc.Screen(
    'invitro',
    profile_filter_args = {'min_ratio': .3},
)
s0.set_results_dir()
s0.read_covariates()
s0.experiment = ('RLBP1', '')
s0.protein = 'RLBP1'
s0.ionmode = 'pos'
s0.peak_version = ''
s0.exp_str = 'RLBP1'
s0.collect_peaks_files()
s0.set_sample_id_proc()
s0.set_ms2_param()


# with E5:E6 ratio
s0.protein_fractions[('RLBP1', '')]['protein_frac0'] = ('E5',)
s0.protein_fractions[('RLBP1', '')]['protein_frac1'] = ('E6',)
s0.setup_data()
s0.one_experiment()


_ = shutil.move(
    os.path.join('plots', 'RLBP1_pos_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_pos_2.00_E5-E6_profiles.png'),
)

_ = shutil.move(
    os.path.join('plots', 'RLBP1_neg_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_neg_2.00_E5-E6_profiles.png'),
)
_ = shutil.move(
    os.path.join(s0.results_dir, 'RLBP1.xlsx'),
    os.path.join(s0.results_dir, 'RLBP1_E5-E6.xlsx'),
)


# with E4:E5 ratio
s0.protein_fractions[('RLBP1', '')]['protein_frac0'] = ('E5',)
s0.protein_fractions[('RLBP1', '')]['protein_frac1'] = ('E4',)
s0.setup_data()
s0.one_experiment()


_ = shutil.move(
    os.path.join('plots', 'RLBP1_pos_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_pos_2.00_E4-E5_profiles.png'),
)

_ = shutil.move(
    os.path.join('plots', 'RLBP1_neg_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_neg_2.00_E4-E5_profiles.png'),
)
_ = shutil.move(
    os.path.join(s0.results_dir, 'RLBP1.xlsx'),
    os.path.join(s0.results_dir, 'RLBP1_E4-E5.xlsx'),
)


# with E6:E7 ratio
s0.protein_fractions[('RLBP1', '')]['protein_frac0'] = ('E6',)
s0.protein_fractions[('RLBP1', '')]['protein_frac1'] = ('E7',)
s0.setup_data()
s0.one_experiment()

_ = shutil.move(
    os.path.join('plots', 'RLBP1_pos_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_pos_2.00_E6-E7_profiles.png'),
)

_ = shutil.move(
    os.path.join('plots', 'RLBP1_neg_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_neg_2.00_E6-E7_profiles.png'),
)
_ = shutil.move(
    os.path.join(s0.results_dir, 'RLBP1.xlsx'),
    os.path.join(s0.results_dir, 'RLBP1_E6-E7.xlsx'),
)



# with E6:E7 and E5:E6 ratios
s0.protein_fractions[('RLBP1', '')]['protein_frac0'] = ('E5', 'E6',)
s0.protein_fractions[('RLBP1', '')]['protein_frac1'] = ('E7',)
s0.setup_data()
s0.one_experiment()

_ = shutil.move(
    os.path.join('plots', 'RLBP1_pos_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_pos_2.00_E5-E6-E7_profiles.png'),
)

_ = shutil.move(
    os.path.join('plots', 'RLBP1_neg_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_neg_2.00_E5-E6-E7_profiles.png'),
)
_ = shutil.move(
    os.path.join(s0.results_dir, 'RLBP1.xlsx'),
    os.path.join(s0.results_dir, 'RLBP1_E5-E6-E7.xlsx'),
)



# with E4:E5 and E5:E6 ratios
s0.protein_fractions[('RLBP1', '')]['protein_frac0'] = ('E5', 'E6',)
s0.protein_fractions[('RLBP1', '')]['protein_frac1'] = ('E4',)
s0.setup_data()
s0.one_experiment()

_ = shutil.move(
    os.path.join('plots', 'RLBP1_pos_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_pos_2.00_E4-E5-E6_profiles.png'),
)

_ = shutil.move(
    os.path.join('plots', 'RLBP1_neg_2.00_profiles.png'),
    os.path.join('plots', 'RLBP1_neg_2.00_E4-E5-E6_profiles.png'),
)
_ = shutil.move(
    os.path.join(s0.results_dir, 'RLBP1.xlsx'),
    os.path.join(s0.results_dir, 'RLBP1_E4-E5-E6.xlsx'),
)
