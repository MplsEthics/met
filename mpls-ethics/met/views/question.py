import logging
from google.appengine.ext import webapp
from met.decorators import ordered
from met.model import Scenario
from met.session import LearnerState
from met.exceptions import InvalidAnswerException
from met.views.base import SecureView


class Question(SecureView):
    """View a question."""

    def assert_scenario_order(self, scenario_id):
        """If the learner is trying to access the questions out of order,
        redirect to the first incomplete scenario."""
        if not self.prereqs_completed(scenario_id):
            incomplete = self.first_incomplete_scenario()
            self.redirect("/%s/intro1" % incomplete)

    @ordered
    def get(self, scenario_id):
        """Show the scenario question to the user."""
        state = LearnerState()
        scenario = state.annotate_scenario(scenario_id)
        path = self.viewpath(append='scenario.djt')
        is_completed = state.is_completed(scenario_id)
        context = dict(s=scenario,
                       session=state.session_fmt(),
                       previous=self.previous(),
                       next=self.next(),
                       show_prevnext=is_completed)
        output = webapp.template.render(path, context)
        self.response.out.write(output)

    @ordered
    def post(self, scenario_id):
        """Process the learner's answer; redirect as appropriate."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)

        # update the session as needed based on the answer
        state = LearnerState()

        # record the answer and redirect
        try:
            answer_id = self.request.params.get('answer', '')
            state.record_answer(scenario_id, answer_id)
        except InvalidAnswerException:
            logging.info("caught invalid answer ID '%s'" % answer_id)
            self.redirect("/%s/question" % scenario_id)
        else:
            self.redirect("/%s/response" % scenario_id)
