#!/usr/bin/python

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
Script to convert YAML files into CSV.
"""

import os
import sys
import yaml
import pprint
import csv

content_ = os.path.join(os.path.dirname(__file__), '../lib')
sys.path.append(content_)

#from met.content import Scenario
import schema
#import pdb; pdb.set_trace()

# scenario writer
sw_cols = ['id', 'name', 'scenario', 'question', 'prompt']
sw = csv.DictWriter(open('scenario.csv', 'w'),
                    sw_cols,
                    extrasaction='ignore')

# answer writer
aw_cols = ['id', 'scenario', 'answer', 'is_correct', 'response']
aw = csv.DictWriter(open('answers.csv', 'w'),
                    aw_cols,
                    extrasaction='ignore',)


def to_utf8(dict_):
    d = dict(dict_)
    for key, value in d.items():
        if isinstance(value, basestring):
            d[key] = value.encode("utf-8")
    return d


def self_dict(list_):
    """Convert list to dict."""
    items = [(x, x) for x in list_]
    return dict(items)


if __name__ == '__main__':
    # write the header columns
    sw.writerow(to_utf8(self_dict(sw_cols)))
    aw.writerow(to_utf8(self_dict(aw_cols)))

    for f in sys.argv[1:]:
        print "converting '%s' to CSV..." % f
        fh = open(f)
        objects = [x for x in yaml.load_all(fh)]
        scenario = objects[0]
        sw.writerow(to_utf8(scenario.__dict__))
        for ans in scenario.answers:
            ans.scenario = scenario.id
            aw.writerow(to_utf8(ans.__dict__))
