#!/usr/bin/env python2.6

"""
The exam portion of the Ethics training.
"""

import json

class SceneTemplate(object):
    pass

class Scene(object):
    pass

class Question(object):

    def __init__(self,name):
        self.name = name

#   name
#   stem
#   answers
#   scenario

class Answer(object):
    pass


class TestBank(object):
    pass


if __name__ == "__main__":
    print "aggle"
    f = open('questions/conflict-of-interest.json')
    js = json.load(f)

