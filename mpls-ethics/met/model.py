#!/usr/bin/env python2.4

from google.appengine.ext import db


class Completion(db.Model):
    """This class models an object for recording a learner's completion of the
    ethics training."""
    name = db.StringProperty(verbose_name='Learner Name')
    board = db.StringProperty(verbose_name='Learner Board or Commission')
    date = db.DateTimeProperty(verbose_name='Completion Timestamp',
        auto_now_add=True)


class Scenario(db.Model):
    """This class models a scenario, which may contain one or more
    Questions."""

    text = db.StringProperty()

    # question_set


class Question(db.Model):
    """This class models a question, which contains many Answers."""

    scenario = db.ReferenceProperty(Scenario)

    stem = db.StringProperty()
    prompt = db.StringProperty()

    # answer_set


class Answer(db.Model):
    """This class models an answer."""

    question = db.ReferenceProperty(Question)
    answer = db.StringProperty()
    is_correct = db.BooleanProperty()
    response = db.StringProperty()
