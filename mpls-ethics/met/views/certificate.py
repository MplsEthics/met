import datetime
from google.appengine.ext import webapp

from met.views.base import SessionView
from met.version import version as VERSION

class Certificate(SessionView):
    """View class for the certificate."""

    def get(self, *argv):
        path = self.viewpath(append='certificate.djt')
        show_prevnext = False
        version = VERSION
        now = datetime.datetime.now()
        session = self.get_session()
        learner_name = session.get('learner_name',None)
        learner_board = session.get('learner_board',None)
        self.response.out.write(webapp.template.render(path, locals()))
