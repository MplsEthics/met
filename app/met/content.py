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

def merge_scenario(id,session):
    """Merge the scenario data with the relevant session data.  This function
    does quite a bit; it should definitely be refactored."""
    scenario = get_scenario(id)

    # find the user's answers to this scenario, if any
    user_answers = session.get(id,[])

    # assume the scenario is not completed unless proven otherwise
    setattr(scenario,"completed",False)

    # set the answer CSS classes
    for a in scenario.answers:
        if a.id not in user_answers:        # unanswered
            setattr(a,"class","answer")
            setattr(a,"disabled",False)
        elif a.correct and a.id in user_answers:
            setattr(a,"class","answer correct")
            setattr(a,"disabled",True)
            setattr(a,"checked",True)
            setattr(scenario,"completed",True)
            setattr(scenario,"response",a.response)
        else:
            setattr(a,"class","answer incorrect")
            setattr(a,"disabled",True)

    # if the scenario has been completed, disable all user inputs, and set the
    # user response to the correct value
    if scenario.completed:
        for a in scenario.answers:
            setattr(a,"disabled",True)
            if a.correct:
                setattr(a,"class","answer correct")
                setattr(scenario,"response",a.response)
            else:
                setattr(a,"class","answer incorrect")

    # make sure the response is for the most recent answer
    try:
        last_answer = user_answers[-1]
    except:
        last_answer = None
    if last_answer is not None:
        for a in scenario.answers:
            if a.id == last_answer:
                setattr(scenario,"response",a.response)
                setattr(a,"checked",True)

    return scenario

if __name__ == '__main__':
    print 'file: %s' % __file__
    pprint(testbank)

