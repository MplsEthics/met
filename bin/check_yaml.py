#!/usr/bin/env python

"""
Script to check formatting of YAML files.
"""

import sys
import yaml


for f in sys.argv[1:]:
    # pylint: disable-msg=E1101
    try:
        print "Checking YAML file '%s'..." % f,  # no newline
        fh = open(f)
        yaml.load_all(fh)
        print " success."
    except yaml.error.YAMLError, e:
        if hasattr(e, 'problem_mark'):
            m = e.problem_mark
            x = (f, m.line + 1, m.column + 1)
            print "Error in file '%s', line %s, column %s" % x
