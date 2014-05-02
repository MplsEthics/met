#!/usr/bin/python

# Copyright 2012 John J. Trammell.
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

import sys
import yaml
import csv

_TRUE = ("true","t","y","yes","1",1)


# scenario writer
sw_cols = ['id', 'name', 'prereq', 'scenario', 'question', 'prompt']
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


class Scenario(yaml.YAMLObject):

    yaml_tag = '!scenario'
    name = 'foo'
    description = 'bar'

    def __init__(self,name,description):
        self.name = name
        self.description = description

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'id': self.id
        }
        return """%(class)s("%(id)s")""" % repr


class Answer(yaml.YAMLObject):

    yaml_tag = '!answer'

    checked = False
    disabled = False

    def __init__(self,_id,answer,is_correct,response):
        self.id = _id
        self.answer = answer
        self.is_correct = is_correct.lower() in _TRUE
        self.response = response

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'id': self.id,
        }
        return "%(class)s(%(id)s)" % repr

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
