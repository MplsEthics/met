#!/usr/bin/env python

# Copyright 2010 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics
# is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

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
