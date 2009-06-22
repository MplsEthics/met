#!/usr/bin/env python

from sys import argv
import yaml


for file in argv[1:]:
    print "Opening file: '%s':\n" % file
    fh = open(file)
    yaml.safe_load(fh)

