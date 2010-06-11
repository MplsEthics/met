#!/usr/bin/python

"""
Script to convert YAML files into CSV.
"""

import os
import sys
import yaml
import pprint

content_ = os.path.join(os.path.dirname(__file__),'../lib/content')
sys.path.append(content_)

#from met.content import Scenario
import schema
#import pdb; pdb.set_trace()

for f in sys.argv[1:]:
    print "Opening YAML file '%s'..." % f,  # no newline
    fh = open(f)
    objects = [x for x in yaml.load_all(fh)]
    pprint.pprint(objects)

