from google.appengine.ext import webapp
import base
from datetime import datetime
from met import content
from met import session

class Scenario(base.BaseView, session.SessionMixin):

    def get(self,scenario_id):
        session = self.getSession()
        scenario = content.merge_scenario(scenario_id,session)

        # persist scenario completion
        if scenario.completed:
            completed = session.get("completed",{})
            completed[scenario_id] = datetime.now()
            session["completed"] = completed

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
        self.assert_scenario_order(scenario_id)
        scenario = content.get_scenario(scenario_id)
        session = self.getSession()
        answer = self.request.params.get('answer',None)
        if answer is not None:
            prev_answers = session.get(scenario_id,[])
            if answer not in prev_answers:
                session[scenario_id] = prev_answers + [answer]
        self.redirect("/%s/response" % scenario_id)

    def assert_scenario_order(self,scenario_id):
        """If the user is accessing this scenario out of order, redirect to
        the most recently completed scenario."""
        # FIXME
        return True

