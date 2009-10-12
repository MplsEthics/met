#!/usr/bin/env python2.5

"""
Classes and other utilities related to dynamic question content.
"""

import os
import yaml
import logging
from pprint import pprint

content_dir = os.path.join(os.path.dirname(__file__), '../content')

class Question(yaml.YAMLObject):

    yaml_tag = '!question'

    def __init__(self,id_,name,prompt,stem,answers):
        self.id = id_
        self.name = name
        self.question = question
        self.prompt = prompt
        self.answers = answers

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'id': self.id,
            'name': self.name,
            'answers': self.answers,
        }
        return """%(class)s("%(name)s")[%(answers)s]""" % repr

    def is_correct(self,answer_id):
        for answer in self.answers:
            if answer.id == answer_id and answer.correct:
                return True
        return False

class Answer(yaml.YAMLObject):

    yaml_tag = '!answer'

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

# load the test bank
testbank = {}
for file in os.listdir(content_dir):
    path = os.path.join(content_dir,file)
    fh = open(path)
    try:
        logging.info("loading file '%s'" % path)
        objects = [x for x in yaml.load_all(fh)]
        question = objects[0]
        question.answers = objects[1:]
    except:
        logging.error("error loading '%s', skipping" % path)
    else:
        testbank[question.id] = question

def get_scenario(id):
    return testbank.get(id,None)

if __name__ == '__main__':
    print 'file: %s' % __file__
    pprint(testbank)

