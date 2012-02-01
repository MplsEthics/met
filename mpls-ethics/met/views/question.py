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

import logging
from google.appengine.ext import webapp
from met.decorators import ordered
from met.session import LearnerState
from met.exceptions import InvalidAnswerException
from met.views.base import BaseView


class Question(BaseView):
    """View a question."""

    @ordered
    def get(self, scenario_id):
        """Show the scenario question to the user."""
        state = LearnerState()
        scenario = state.annotate_scenario(scenario_id)
        path = self.viewpath(append='scenario.djt')
        is_completed = state.is_completed(scenario_id)
        context = dict(s=scenario,
                       state=state.as_string(),
                       previous=self.previous(),
                       next=self.next(),
                       show_prevnext=is_completed)
        output = webapp.template.render(path, context)
        self.response.out.write(output)

    @ordered
    def post(self, scenario_id):
        """Process the learner's answer; redirect as appropriate."""
        state = LearnerState()
        try:
            answer_id = self.request.params.get('answer', '')
            state.record_answer(scenario_id, answer_id)
        except InvalidAnswerException:
            logging.info("caught invalid answer ID '%s'" % answer_id)
            self.redirect("/%s/question" % scenario_id)
        else:
            self.redirect("/%s/response" % scenario_id)
