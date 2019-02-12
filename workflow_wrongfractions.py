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

import numpy as np

from ltp import featureproc
from lipyd import ms2
from lipyd import sample
from lipyd import feature


def reload():
    
    imp.reload(ms2)
    imp.reload(sample)
    imp.reload(feature)
    imp.reload(featureproc)


def load(protein, ionmode, peak_version = ''):
    
    s0 = featureproc.Screen('invitro', )
    s0.set_results_dir()
    s0.read_covariates()
    s0.experiment = (protein, '')
    s0.protein = protein
    s0.ionmode = ionmode
    s0.peak_version = peak_version
    s0.exp_str = protein
    s0.collect_peaks_files()
    s0.set_sample_id_proc()
    s0.set_ms2_param()
    s0.setup_data()
    
    return s0


def print_total_intensities(protein, ionmode, peak_version = ''):
    
    s0 = load(protein, ionmode, peak_version = peak_version)
    
    itotals = np.nansum(s0.samples.intensities, axis = 0)
    s0.basic_filters()
    fenums = (s0.samples.intensities > 0).sum(axis = 0)
    
    print('\n'.join(
        '%s%u:\t%u\t%u' % (row, col, int(itotal), fenum)
        for (row, col), itotal, fenum in
        zip(
            s0.samples.attrs.sample_index_to_id,
            itotals,
            fenums,
        )
    ))


print_total_intensities('CLVS1', 'pos')

#A0:	3023426942	1289
#A4:	3054683294	1531
#A5:	2911986228	1397
#A6:	2850423728	1428
#A7:	2845750710	1230 *
#A8:	2719087067	1348
#A9:	2711862348	1200
#A10:	2768046748	1258
#A11:	2752685115	1174


print_total_intensities('FABP4', 'neg')

#G0:	170748269	269
#G5:	181966312	279
#G6:	150979430	279
#G7:	171362321	276
#G8:	165273119	281
#G9:	178500970	275
#G10:	173325882	278
#G11:	103068061	209 *
#G12:	170967837	282
#H1:	234082553	267


print_total_intensities('FABP6', 'neg')

#A0:	216668941	352
#A5:	177691815	333
#A6:	207614130	351
#A7:	188022515	366
#A8:	 85431669	239 *
#A9:	218841108	363
#A10:	229390343	364
#A11:	219519318	356
#A12:	210669742	349


print_total_intensities('GLTPD1', 'neg')

#E0:	113212995	189
#E3:	290905277	356
#E4:	290898915	356
#E5:	273191755	349
#E6:	266616941	357
#E7:	275999216	359
#E8:	330343476	367
#E9:	 94488895	191 *
#E10:	283605323	349
#E11:	280651063	345
#E12:	108341384	189


print_total_intensities('GM2A', 'neg')

#G0:	298482538	301
#G7:	142223583	218
#G8:	339575048	321
#G9:	272591873	326
#G10:	244693378	321
#G11:	304550674	311
#G12:	152870277	215 *
#H1:	182906735	217


print_total_intensities('GM2A', 'pos')

#G0:	3417498363	1876
#G7:	3316086481	2008
#G8:	3533169322	1279
#G9:	3329613910	2019
#G10:	3400976747	1316 *
#G11:	3445894987	1830
#G12:	3175039859	1972
#H1:	3117979075	1919


print_total_intensities('HSDL2', 'neg', 'a')

#A0:	130180994	172
#A4:	286183401	285
#A5:	110479151	168 *
#A6:	220238985	271 *
#A7:	135374858	169
#A8:	258321715	270
#A9:	135257913	160
#A10:	268231041	271


print_total_intensities('RBP7', 'neg')

#C0:	254041147	336
#C5:	111555133	254
#C6:	235202847	347
#C7:	229982727	354
#C8:	116009961	256 *
#C9:	236762474	373
#C10:	129054989	256 *
#C11:	226972965	364
#C12:	244552629	358


print_total_intensities('SEC14L2', 'neg')

#C0:	265581257	269
#C5:	169493710	214
#C6:	387011213	304
#C7:	131845395	279
#C8:	128894213	218 *
#C9:	389521026	329
#C10:	295408190	339
#C11:	169858904	219 *
#C12:	173552702	220


print_total_intensities('SEC14L2', 'pos')

#C0:	3214025950	1741
#C5:	3267696769	1277
#C6:	3276298666	1281
#C7:	3122481556	1959
#C8:	3176962230	1910
#C9:	2638350810	1292 *
#C10:	2619642722	1932
#C11:	3231075995	1846
#C12:	3354516096	1297


print_total_intensities('SEC14L5', 'pos')

#A0:	2430378757	1126
#A4:	2531794512	 624 *
#A5:	2627873605	1302
#A6:	2496956993	 600 *
#A7:	2687011299	1314
#A8:	2554460577	 594 *
#A9:	2612250071	1343
#A10:	2495148777	1224
#A11:	2557087343	 584
