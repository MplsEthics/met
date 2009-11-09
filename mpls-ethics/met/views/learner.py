import logging
from datetime import datetime
from google.appengine.ext.webapp import template
from met import order, session
from met.boards import boards as boards_
from met.email import send_completion
from met.model import Completion
from met.views import base

class Learner(base.BaseView, session.SessionMixin, order.OrderMixin):

    def get(self):
        path = self.viewpath(append='learner.djt')
        session = self.getSession()
        show_prevnext = True
        boards = boards_
        learner_error = self.request.params.get('learner_error',None)
        self.response.out.write(template.render(path,locals()))

    def post(self):
        """Process the learner data submission, then redirect to the
        'certificate' view."""

        session = self.getSession()

        # ensure that all scenarios have been completed FIXME
        # self.assert_scenario_order(scenario_id,session)

        # update the session as needed based on the answer
        learner_name = self.request.params.get('learner_name',None)
        learner_board = self.request.params.get('learner_board',None)

        # bail if we don't have both name and board
        if learner_name is None or learner_board is None:
            session["learner_error"] = True
            self.redirect('/learner')

        # persist the learner name and board in the session
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

