#!/usr/bin/env python2.6

"""
The exam portion of the Ethics training.
"""

import yaml

class Question(yaml.YAMLObject):

    yaml_tag = u'!Question'

    def __init__(self,name,prompt,stem,answers):
        self.name = name
        self.prompt = prompt
        self.stem = stem
        self.answers = answers

    def __repr__(self):
        return "%s(%s)[%s]" % (self.__class__.__name__,self.name,self.answers)

class Answer(yaml.YAMLObject):

    yaml_tag = u'!Answer'

    def __init__(self,answer,response,correct):
        self.answer = answer
        self.response = response
        self.correct = correct

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__,self.answer)

testbank = []

def load_testbank():

    fh = open(file)
    pprint(yaml.load(fh))

