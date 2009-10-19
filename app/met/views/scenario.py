from google.appengine.ext import webapp
import base
from datetime import datetime
from met import content
from met import session
from met.order import scenario_order

class Scenario(base.BaseView, session.SessionMixin):

    def get(self,scenario_id):
        session = self.getSession()
        self.assert_scenario_order(scenario_id,session)
        scenario = content.merge_scenario(scenario_id,session)


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
        session = self.getSession()
        self.assert_scenario_order(scenario_id,session)
        scenario = content.get_scenario(scenario_id)

        # update the session as needed based on the answer
        answer = self.request.params.get('answer',None)
        if answer is not None:
            # save the answer
            if answer not in session[scenario_id]:
                session[scenario_id].append(answer)

            # if the answer is correct, update session.completed
            answer_obj = scenario.answer_dict.get(answer,None)
            if answer_obj.correct:
                session["completed"][scenario_id] = datetime.now()

        self.redirect("/%s/response" % scenario_id)

    def assert_scenario_order(self,scenario_id,session):
        """If the user is accessing this scenario out of order, redirect to
        the most recently completed scenario."""
        for i in range(scenario_order.index(scenario_id)):
            test_scenario = scenario_order[i]
            if test_scenario not in session['completed']:
                self.redirect("/%s/response" % test_scenario)

