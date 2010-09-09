from datetime import datetime
from google.appengine.ext import webapp
from met.decorators import ordered
from met.views.base import SessionView
from met.version import version


class Certificate(SessionView):
    """View class for the certificate."""

    @alldone
    def get(self, *argv):
        path = self.viewpath(append='certificate.djt')
        context = dict(show_prevnext=False,
                       version=version,
                       now=datetime.now(),
                       session=state.session_fmt(),
                       learner_name=session.get('learner_name', None),
                       learner_board=session.get('learner_board', None))
        output = webapp.template.render(path, context)
        self.response.out.write(output)
