from google.appengine.ext import webapp
from met.content import InvalidAnswerError, LearnerScenario
from met.views.base import SecureView

class Scenario(SecureView):

    def assert_scenario_order(self,scenario_id):
        """If the learner is trying to access this scenario out of order,
        redirect to the first incomplete scenario."""
        compdict = self.getSession()['completed']
        if not self.prereqs_completed(scenario_id):
            incomplete = self.first_incomplete_scenario()
            self.redirect("/%s/intro1" % incomplete)

    def get(self,scenario_id):
        """Handle HTTP GET--show the scenario question to the user."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)

        # retreive the merged scenario / session object
        ls = LearnerScenario(scenario_id,self.getSession())

        # render the template
        path = self.viewpath(append='scenario.djt')
        djt = dict(s=ls,
                   previous=self.previous(),
                   next=self.next(),
                   show_prevnext=ls.is_completed())
        self.response.out.write(webapp.template.render(path,djt))

    def post(self,scenario_id):
        """Process the answer submission, then redirect to the "response"
        view."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)

        # update the session as needed based on the answer
        ls = LearnerScenario(scenario_id,self.getSession())

        # record the answer and redirect
        try:
            answer_id = self.request.params.get('answer',None)
            ls.record_answer(answer_id)
        except InvalidAnswerError:
            self.redirect("/%s/scenario" % scenario_id)
        else:
            self.redirect("/%s/response" % scenario_id)

