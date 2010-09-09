import logging
from google.appengine.ext.webapp import template
from met.boards import boards
from met.email import send_completion
from met.model import Completion
from met.views.base import SecureView
from met.session import LearnerState


class Learner(SecureView):

    @alldone
    def get(self):
        path = self.viewpath(append='learner.djt')
        learner_error = session.get('learner_error', False)
        context = dict(show_prevnext=True,
                       boards=boards,
                       learner_error=learner_error,
                       session=state.session_fmt())
        output = template.render(path, context)
        self.response.out.write(output)

    @alldone
    def post(self):
        """Persist the learner data in the GAE datastore and in the session,
        then send the email and redirect to the 'certificate' view."""

        state = LearnerState()

        # persist the learner data
        try:
            name = self.request.params.get('learner_name', "")
            board_id = self.request.params.get('learner_board_id', "")
            state.persist_learner(name, board_id)
        except InvalidLearnerException:
            session["learner_error"] = True
            self.redirect('/learner')
            return

        # send the completion email
        try:
            send_completion(learner_name, learner_board)
        except:
            pass

        # redirect to the certificate view
        self.redirect('/certificate')

# FIXME: cleanup

        # update the session as needed based on the answer

        # bail if we don't have a valid learner name
        learner_name = self.request.params.get('learner_name', "")
        if len(learner_name) == 0:
            session["learner_error"] = True
            self.redirect('/learner')
            return

        # bail if we don't have a valid learner board
        learner_board_id = self.request.params.get('learner_board_id', "")
        try:
            learner_board = boards_[int(learner_board_id)]
            if len(learner_board) == 0:
                raise
        except:
            session["learner_error"] = True
            self.redirect('/learner')
            return

        # persist the learner name and board in the session (to be used by the
        # certificate template)
        session["learner_name"] = learner_name
        session["learner_board"] = learner_board

        # persist the learner name, board, and timestamp in GAE storage
        # (timestamp should be created automatically)
        comp = Completion()
        comp.name = learner_name
        comp.board = learner_board
        comp.put()

        # send the completion email
        try:
            send_completion(learner_name, learner_board)
        except:
            pass

        # redirect to the certificate view
        self.redirect('/certificate')
