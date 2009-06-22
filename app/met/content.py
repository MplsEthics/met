#!/usr/bin/env python2.6

"""
The exam portion of the Ethics training.
"""

import yaml

class SceneTemplate(object):
    pass

class Scene(object):
    pass

class Question(yaml.YAMLObject):

    yaml_tag = u'!Question'

    def __init__(self,name,prompt,stem,answers):
        self.name = name
        self.prompt = prompt
        self.stem = stem
        self.answers = answers

    def __repr__(self):
        return "%s(%s)[%s]" % (self.__class__.__name__,self.name,self.answers)

#   name
#   stem
#   answers
#   scenario

class Answer(yaml.YAMLObject):

    yaml_tag = u'!Answer'

    def __init__(self,answer,response,correct):
        self.answer = answer
        self.response = response
        self.correct = correct

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__,self.answer)


class TestBank(object):
    pass


if __name__ == "__main__":
    print "aggle"
    f = open('questions/conflict-of-interest.json')
    js = json.load(f)

