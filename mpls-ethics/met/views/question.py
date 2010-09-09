from google.appengine.ext import webapp
from met.content import InvalidAnswerError, LearnerScenario
from met.views.base import SecureView

class Question(SecureView):

    def assert_scenario_order(self,scenario_id):
        """If the learner is trying to access the questions out of order,
        redirect to the first incomplete scenario."""
        compdict = self.get_session()['completed']
        if not self.prereqs_completed(scenario_id):
            incomplete = self.first_incomplete_scenario()
            self.redirect("/%s/intro1" % incomplete)

    def get(self, scenario_id):
        """Handle HTTP GET--show the scenario question to the user."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)
        # retreive the merged scenario / session object
        session = self.get_session()
        ls = LearnerScenario(scenario_id, session)

        # render the template
        path = self.viewpath(append='scenario.djt')
        djt = dict(s=ls,
                   session=session,
                   previous=self.previous(),
                   next=self.next(),
                   show_prevnext=ls.is_completed())
        self.response.out.write(webapp.template.render(path, djt))

    def post(self, scenario_id):
        """Process the learner's answer; redirect as appropriate."""
        # enforce correct scenario order
        self.assert_scenario_order(scenario_id)

        # update the session as needed based on the answer
        ls = LearnerScenario(scenario_id, self.get_session())

        # record the answer and redirect
        try:
            answer_id = self.request.params.get('answer','')
            ls.record_answer(answer_id)
        except InvalidAnswerError:
            self.redirect("/%s/question" % scenario_id)
        else:
            self.redirect("/%s/response" % scenario_id)
