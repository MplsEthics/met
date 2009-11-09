#!/usr/bin/env python

"""
Script to check formatting of YAML files.
"""

import os
#import re
import sys
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__),'../mpls-ethics'))

#from met import content
#import pdb; pdb.set_trace()

for f in sys.argv[1:]:
    # pylint: disable-msg=E1101
    try:
        print "Opening YAML file '%s'..." % f,  # no newline
        fh = open(f)
        yaml.load_all(fh)
        print " success.\n"
    except yaml.error.YAMLError, e:
        if hasattr(e, 'problem_mark'):
            m = e.problem_mark
            x = (f, m.line + 1, m.column + 1)
            print "Error in file '%s', line %s, column %s" % x

