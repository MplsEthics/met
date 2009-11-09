from google.appengine.ext import webapp
import base
from datetime import datetime
from met import content, order, session
import time

class Scenario(base.SecureView):

    def get(self,scenario_id):
        """Handle HTTP GET--show the scenario question to the user."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)

        # retreive the merged scenario / session object
        session = self.getSession()
        scenario = content.merge_scenario(scenario_id,session)

        # render the template
        path = self.viewpath(append='scenario.djt')
        djt = {
            'previous': self.previous(),
            'next': self.next(),
            's': scenario,
            'session': session,
            'show_prevnext': scenario.completed,
        }
        self.response.out.write(webapp.template.render(path,djt))

    def post(self,scenario_id):
        """Process the answer submission, then redirect to the "response"
        view."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)

        # update the session as needed based on the answer
        session = self.getSession()
        scenario = content.get_scenario(scenario_id)
        valid_answer_ids = scenario.answer_dict.keys()

        # get the learner's answer from the request object
        answer_id = self.request.params.get('answer',None)

        # if we don't have a valid answer ID, re-GET the scenario
        if answer_id not in valid_answer_ids:
            self.redirect("/%s/scenario" % scenario_id)
            return

        # we have a valid answer ID; record it
        if answer_id not in session[scenario_id]:
            learner_answers = session[scenario_id]
            learner_answers.append(answer_id)
            session[scenario_id] = learner_answers

        # if the answer is correct, also update session['completed']
        answer_obj = scenario.answer_dict[answer_id]
        if answer_obj.correct:
            completed = session["completed"]
            completed[scenario_id] = datetime.now().isoformat()
            session["completed"] = completed

        # redirect to the response page
        self.redirect("/%s/response" % scenario_id)

    def assert_scenario_order(self,scenario_id):
        """If the learner is trying to access this scenario out of order,
        redirect to the first incomplete scenario."""
        compdict = self.getSession()['completed']
        if not self.prereqs_completed(scenario_id):
            incomplete = self.first_incomplete_scenario()
            self.redirect("/%s/intro1" % incomplete)

