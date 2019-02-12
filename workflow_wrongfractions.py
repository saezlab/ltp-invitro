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
from lipyd import ms2
from lipyd import sample
from lipyd import feature


def reload():
    
    imp.reload(ms2)
    imp.reload(sample)
    imp.reload(feature)
    imp.reload(featureproc)


def load(protein, ionmode):
    
    s0 = featureproc.Screen('invitro', )
    s0.set_results_dir()
    s0.read_covariates()
    s0.experiment = (protein, '')
    s0.protein = protein
    s0.ionmode = ionmode
    s0.peak_version = ''
    s0.exp_str = protein
    s0.collect_peaks_files()
    s0.set_sample_id_proc()
    s0.set_ms2_param()
    s0.setup_data()
    
    return s0
