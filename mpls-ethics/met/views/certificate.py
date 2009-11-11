import os
import logging
import datetime
import base
from google.appengine.ext import webapp
from met.version import version as VERSION

class Certificate(base.SessionView):
    """View class for the certificate."""

    def get(self, *argv):
        path = self.viewpath(append='main.djt')
        show_prevnext = False
        version = VERSION
        now = datetime.datetime.now()
        session = self.getSession()
        learner_name = session.get('learner_name',None)
        learner_board = session.get('learner_board',None)
        self.response.out.write(webapp.template.render(path,locals()))

