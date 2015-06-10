# Copyright 2015 John J. Trammell.
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

from met.exceptions import InvalidLearnerException
from met.views.base import BaseView
from met.state import LearnerState
from met.model import Board


class Cheater(BaseView):
    """
    This is a view to skip ahead to the certificate of completion, for testing
    purposes.
    """

    def get(self):
        state = LearnerState(self.session)
        learner_error = state.learner_error()
        context = dict(show_prevnext=True,
                       boards=Board.all().order('priority'),
                       learner_error=learner_error,
                       cheater=True,
                       state=state.as_string())
        jt = self.jinja_environment().get_template('learner.djt')
        self.response.write(jt.render(context))

    def post(self):
        """
        Attempt to persist the learner data in the GAE datastore and in the
        session, send the email, and redirect to the certificate view.
        """
        state = LearnerState(self.session)

        # persist the learner data
        try:
            name = self.request.params.get('learner_name', "")
            board_id = self.request.params.get('learner_board_id', "")
            date = self.request.params.get('learner_date', "")
            state.persist_learner(name, board_id, date)
        except InvalidLearnerException:
            self.redirect('/cheater')
            return

        # redirect to the certificate view
        self.redirect('/certificate')
