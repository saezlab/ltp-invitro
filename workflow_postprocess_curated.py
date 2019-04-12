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
#  Website: http://www.ebi.ac.uk/~denes
#

import imp
import os

from lipyd import settings
from lipyd import lipproc
from lipyd import name
from lipyd import moldb
from lipyd import mz
from lipyd import mass
from lipyd import formula
from ltp import results
from ltp import ltproteins
from ltp import settings as ltpsettings


def reload():
    
    imp.reload(settings)
    imp.reload(ltpsettings)
    imp.reload(mz)
    imp.reload(mass)
    imp.reload(formula)
    imp.reload(lipproc)
    imp.reload(name)
    imp.reload(moldb)
    moldb.db.reload()
    imp.reload(ltproteins)
    imp.reload(results)


reload()
rr = results.ResultsReader(screen = 'invitro')
rr.main()
rr.export()
