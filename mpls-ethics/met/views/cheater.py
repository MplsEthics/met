from google.appengine.ext.webapp import template
from met.boards import boards
from met.exceptions import InvalidLearnerException
from met.views.base import BaseView
from met.session import LearnerState


class Cheater(BaseView):

    def get(self):
        path = self.viewpath(append='learner.djt')
        state = LearnerState()
        learner_error = state.learner_error()
        context = dict(show_prevnext=True,
                       boards=boards,
                       learner_error=learner_error,
                       session=state.session_fmt())
        output = template.render(path, context)
        self.response.out.write(output)

    def post(self):
        """Attempt to persist the learner data in the GAE datastore and in the
        session, send the email, and redirect to the certificate view."""

        state = LearnerState()

        # persist the learner data
        try:
            name = self.request.params.get('learner_name', "")
            board_id = self.request.params.get('learner_board_id', "")
            state.persist_learner(name, board_id)
        except InvalidLearnerException:
            self.redirect('/cheater')
            return

        # redirect to the certificate view
        self.redirect('/certificate')