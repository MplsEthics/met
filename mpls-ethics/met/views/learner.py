# Copyright 2012 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics
# is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

from google.appengine.ext.webapp import template
from met.boards import boards
from met.decorators import alldone
from met.email import send_completion
from met.exceptions import InvalidLearnerException
from met.views.base import BaseView
from met.state import LearnerState


class Learner(BaseView):

    @alldone
    def get(self):
        state = LearnerState(self.session)
        learner_error = state.learner_error()
        context = dict(show_prevnext=True,
                       boards=boards,
                       learner_error=learner_error,
                       state=state.as_string())
        jt = self.jinja_environment().get_template('learner.djt')
        self.response.write(jt.render(context))

    @alldone
    def post(self):
        """
        Attempt to persist the learner data in the appengine datastore and in
        the session, send the email, and redirect to the certificate view.
        """
        state = LearnerState(self.session)

        # persist the learner data
        try:
            name = self.request.params.get('learner_name', "")
            board_id = self.request.params.get('learner_board_id', "")
            state.persist_learner(name, board_id, None)
        except InvalidLearnerException:
            self.redirect('/learner')
            return

        # send the completion email
        try:
            name = state.learner_name()
            board = state.learner_board()
            send_completion(name, board)
        except:
            pass

        # redirect to the certificate view
        self.redirect('/certificate')
