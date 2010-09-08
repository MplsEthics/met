#!/usr/bin/python

"""
Script to convert YAML files into CSV.
"""

import os
import sys
import yaml
import pprint
import csv

content_ = os.path.join(os.path.dirname(__file__),'../lib')
sys.path.append(content_)

#from met.content import Scenario
import schema
#import pdb; pdb.set_trace()

# scenario writer
sw = csv.DictWriter(
    open('scenario.csv','w'),
    ['id','name','scenario','question','prompt'],
    extrasaction='ignore',
)

# answer writer
aw = csv.DictWriter(
    open('answers.csv','w'),
    ['id','scenario','answer','is_correct','response'],
    extrasaction='ignore',
)

def to_utf8(dict_):
    d = dict(dict_)
    for key, value in d.items():
        if isinstance(value,basestring):
            d[key] = value.encode("utf-8")
    return d

if __name__ == '__main__':

    for f in sys.argv[1:]:
        print "converting '%s' to CSV..." % f
        fh = open(f)
        objects = [x for x in yaml.load_all(fh)]
        scenario = objects[0]
        sw.writerow(to_utf8(scenario.__dict__))
        for ans in scenario.answers:
            ans.scenario = scenario.id
            aw.writerow(to_utf8(ans.__dict__))

