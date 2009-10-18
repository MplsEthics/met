from google.appengine.ext import webapp
import base
from met import content
from met import session

class Scenario(base.BaseView, session.SessionMixin):

    def get(self,scenario_id,view):
        if view != 'scenario':
            a = "%s/%s.djt" % (scenario_id, view)
            path = self.viewpath(append=a)
            djt = {
                'next': self.next(),
                'previous': self.previous(),
                's': content.get_scenario(scenario_id),
                'show_prevnext': True,
            }
            self.response.out.write(webapp.template.render(path,djt))
        else:
            self.get_scenario(scenario_id)

    def get_scenario(self,scenario_id):
        session = self.getSession()
        scenario = content.merge_scenario(scenario_id,session)
        path = self.viewpath(append='scenario.djt')
        last_answer = self.most_recent_answer(scenario_id)
        djt = {
            'previous': self.previous(),
            'next': self.next(),
            's': scenario,
            'session': session,
            'show_prevnext': scenario.completed,
        }
        self.response.out.write(webapp.template.render(path,djt))

    def most_recent_answer(self,scenario_id):
        session = self.getSession()
        try:
            return session[scenario_id][-1]
        except:
            return None

    def post(self,scenario_id,view):
        """Process the answer submission, then redirect to the question
        view."""
        scenario = content.get_scenario(scenario_id)
        session = self.getSession()
        answer = self.request.params.get('answer',None)
        if answer is not None:
            prev_answers = session.get(scenario_id,[])
            if answer not in prev_answers:
                session[scenario_id] = prev_answers + [answer]
        self.redirect("/%s/scenario" % scenario_id)

