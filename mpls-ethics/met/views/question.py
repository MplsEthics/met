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

import logging
from google.appengine.ext import webapp
from met.decorators import ordered
from met.state import LearnerState
from met.exceptions import InvalidAnswerException
from met.views.base import BaseView


class Question(BaseView):
    """View a question."""

    @ordered
    def get(self, scenario_id):
        """Show the scenario question to the user."""
        state = LearnerState(self.session)
        scenario = state.annotate_scenario(scenario_id)
        is_completed = state.is_completed(scenario_id)
        context = dict(s=scenario,
                       state=state.as_string(),
                       previous=self.previous(),
                       next=self.next(),
                       show_prevnext=is_completed)
        jt = self.jinja_environment().get_template('scenario.djt')
        self.response.write(jt.render(context))

    @ordered
    def post(self, scenario_id):
        """Process the learner's answer; redirect as appropriate."""
        state = LearnerState(self.session)
        try:
            answer_id = self.request.params.get('answer', '')
            state.record_answer(scenario_id, answer_id)
        except InvalidAnswerException:
            logging.info("caught invalid answer ID '%s'" % answer_id)
            self.redirect("/%s/question" % scenario_id)
        else:
            self.redirect("/%s/response" % scenario_id)
