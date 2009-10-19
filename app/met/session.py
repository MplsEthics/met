#!/usr/bin/env python

"""

"""

from appengine_utilities import sessions
from met.order import scenario_order

class Session(sessions.Session):
    """Subclass the appengine_utilities session object to simplify
    extension."""
    pass

class SessionMixin(object):
    def getSession(self):

        # stash the session object in _session
        if not hasattr(self,'session'):
            self._session = Session()

        # make sure all scenario answer arrays are present
        for s in scenario_order:
            if not s in self._session:
                self._session[s] = []

        # make sure the scenario completion dict is present
        if not 'completed' in self._session:
            self._session['completed'] = dict()

        return self._session

