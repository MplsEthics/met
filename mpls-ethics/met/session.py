#!/usr/bin/env python

"""
This module implements a custom Session class for the Minneapolis Ethics
Training site.  It uses the GAEUtilities sessions class as its basis (see
http://code.google.com/p/gaeutilities/).
"""

from appengine_utilities import sessions

class Session(sessions.Session):
    """Subclass the appengine_utilities session object to simplify
    extension."""
    pass

