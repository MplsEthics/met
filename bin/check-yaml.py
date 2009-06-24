#!/usr/bin/env python

import os
import re
import sys
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__),'../app'))

import met

import pdb; pdb.set_trace()

for file in sys.argv[1:]:
    print "Opening file: '%s':\n" % file
    fh = open(file)
    try:
        yaml.load(fh)
    except yaml.YAMLError, e:
        if hasattr(e, 'problem_mark'):
            m = e.problem_mark
            x = (file, m.line + 1, m.column + 1)
            print "Error in file '%s', line %s, column %s" % x

