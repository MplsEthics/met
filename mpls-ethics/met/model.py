#!/usr/bin/env python2.4

from google.appengine.ext import db

class Completion(db.Model):
    """This class models an object for recording a learner's completion of the
    ethics training."""
    name = db.StringProperty(verbose_name='Learner Name')
    board = db.StringProperty(verbose_name='Learner Board or Commission')
    date = db.DateTimeProperty(verbose_name='Completion Timestamp',
        auto_now_add=True)

