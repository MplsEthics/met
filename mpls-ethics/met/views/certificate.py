from datetime import datetime
from google.appengine.ext import webapp
from met.decorators import alldone
from met.views.base import BaseView
from met.session import LearnerState
from met.version import version


class Certificate(BaseView):
    """View class for the certificate."""

    @alldone
    def get(self, *argv):
        path = self.viewpath(append='certificate.djt')
        state = LearnerState()
        context = dict(show_prevnext=False,
                       version=version,
                       now=datetime.now(),
                       session=state.session_fmt(),
                       learner_name=state.learner_name(),
                       learner_board=state.learner_board())
        output = webapp.template.render(path, context)
        self.response.out.write(output)
