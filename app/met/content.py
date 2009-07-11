#!/usr/bin/env python

"""
The exam portion of the Ethics training.
"""

import os
import yaml
from pprint import pprint

content_dir = os.path.join(os.path.dirname(__file__), '../content')

class Question(yaml.YAMLObject):

    yaml_tag = u'!question'

    def __init__(self,name,prompt,stem,answers):
        self.name = name
        self.prompt = prompt
        self.stem = stem
        self.answers = answers

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'name': self.name,
            'answers': self.answers,
        }
        return u"%(class)s(%(name)s)[%(answers)s]" % repr

class Answer(yaml.YAMLObject):

    yaml_tag = u'!answer'

    def __init__(self,answer,response,correct):
        self.answer = answer
        self.response = response
        self.correct = correct

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'answer': '%s...' % self.answer[0:30],
        }
        return u"%(class)s(%(answer)s)" % repr

# load the test bank
testbank = {}
for file in os.listdir(content_dir):
    path = os.path.join(content_dir,file)
    fh = open(path)
    try:
        print "loading file '%s'" % path
        objects = [x for x in yaml.load_all(fh)]
        question = objects[0]
        question.answers = objects[1:]
    except:
        print "error loading file '%s' ... skipping" % path
    else:
        testbank[question.name] = question

def get_question(id):
    return testbank[id]

if __name__ == '__main__':
    print u'file: %s' % __file__
    pprint(testbank)

