#!/usr/bin/env python2.6

"""
The exam portion of the Ethics training.
"""

import os
import yaml

content_dir = os.path.join(os.path.dirname(__file__), '../content')

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

# load the test bank
testbank = [ None ]
for file in os.listdir(content_dir):
    path = os.path.join(content_dir,file)
    fh = open(path)
    testbank.append(yaml.load(fh))

def get_question(id):
    return testbank[id]

