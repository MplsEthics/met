import logging
from datetime import datetime
from google.appengine.ext.webapp import template
from met import session
from met import boards
from met.views import base
from met.model import Completion

class Learner(base.BaseView, session.SessionMixin):

    def get(self):
        path = self.viewpath(append='learner.djt')
        session = self.getSession()
        show_prevnext = True
        boards = boards.boards
        self.response.out.write(template.render(path,locals()))

    def post(self):
        """Process the learner data submission, then redirect to the
        'certificate' view."""

        session = self.getSession()

        # ensure that all scenarios have been completed FIXME
        self.assert_scenario_order(scenario_id,session)

        # update the session as needed based on the answer
        learner_name = self.request.params.get('learner_name',None)
        learner_board = self.request.params.get('learner_board',None)

        # persist the learner name and board in the session
        session["learner_name"] = learner_name
        session["learner_board"] = learner_board

        # persist the learner name, board, and timestamp in GAE storage
        # (timestamp should be created automatically)
        comp = Completion()
        comp.name = learner_name
        comp.board = learner_board
        comp.put()

        # redirect to the certificate view
        self.redirect('/certificate')

