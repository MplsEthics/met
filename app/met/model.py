#!/usr/bin/env python2.4

"""
"""

from google.appengine.ext import db

class Complete(db.Model):
    """This class models an object for recording a learner's completion of the
    ethics training."""
    name = db.StringProperty()
    department = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

