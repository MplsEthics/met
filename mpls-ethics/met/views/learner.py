import logging
from google.appengine.ext.webapp import template
from met.boards import boards as boards_
from met.email import send_completion
from met.model import Completion
from met.views.base import SecureView

class Learner(SecureView):

    def get(self):
        # ensure that all scenarios have been completed
        self.assert_all_scenarios_completed()

        path = self.viewpath(append='learner.djt')
        session = self.getSession()
        show_prevnext = True
        boards = boards_
        learner_error = session.get('learner_error',False)
        logging.info('''learner_error: "%s"''' % learner_error)
        self.response.out.write(template.render(path,locals()))

    def post(self):
        """Process the learner data submission, then redirect to the
        'certificate' view."""

        session = self.getSession()

        # ensure that all scenarios have been completed
        self.assert_all_scenarios_completed()

        # update the session as needed based on the answer

        # bail if we don't have a valid learner name
        learner_name = self.request.params.get('learner_name',"")
        if len(learner_name) == 0:
            session["learner_error"] = True
            self.redirect('/learner')
            return

        # bail if we don't have a valid learner board
        learner_board_id = self.request.params.get('learner_board_id',"")
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
            send_completion(learner_name,learner_board)
        except:
            pass

        # redirect to the certificate view
        self.redirect('/certificate')

