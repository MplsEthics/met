#!/usr/bin/env python

from sys import argv
import yaml

print 'Opening file: %s' % argv[1]

fh = open(argv[1])

yaml.load(fh)

