#!/usr/bin/env python2.5

"""
Classes and other utilities related to dynamic question content.
"""

import copy
import os
import yaml
import logging
from pprint import pprint


class Topic(yaml.YAMLObject):
    yaml_tag = '!topic'


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
            'name': self.name,
            'desc': self.description,
        }
        return """%(class)s("%(name)s")[%(desc)s]""" % repr


class Question(yaml.YAMLObject):
    yaml_tag = '!question'



class Answer(yaml.YAMLObject):

    yaml_tag = '!answer'

    checked = False
    disabled = False

    def __init__(self,_id,answer,correct,response):
        self.id = _id
        self.answer = answer
        self.correct = correct
        self.response = response

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'answer': '%s...' % self.answer[0:30],
            'id': self.id,
        }
        return "%(class)s(%(id)s:%(answer)s)" % repr

