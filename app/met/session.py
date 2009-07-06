#!/usr/bin/env python

"""

"""

from appengine_utilities import sessions

class Session(sessions.Session):
    """Subclass the appengine_utilities session object to simplify
    extension."""
    pass

class SessionMixin(object):
    def getSession(self):
        if not hasattr(self,'session'):
            self.session = Session()
        return self.session

