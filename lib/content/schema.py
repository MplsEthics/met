#!/usr/bin/env python2.5

"""Schema classes for question content."""

import yaml

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


class Answer(yaml.YAMLObject):

    yaml_tag = '!answer'

    checked = False
    disabled = False

    def __init__(self,_id,answer,is_correct,response):
        self.id = _id
        self.answer = answer
        self.is_correct = is_correct
        self.response = response

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'answer': '%s...' % self.answer[0:30],
            'id': self.id,
        }
        return "%(class)s(%(id)s:%(answer)s)" % repr

