from google.appengine.ext import webapp
import base
from datetime import datetime
from met import content
from met import session

class Response(base.BaseView, session.SessionMixin):

    def get(self,scenario_id):
        session = self.getSession()
        scenario = content.merge_scenario(scenario_id,session)
        answer_id = session[scenario_id][-1]
        path = self.viewpath(append='response.djt')
        if scenario.completed:
            link_next = "/%s/disc1" % scenario_id
        else:
            link_next = "/%s/scenario" % scenario_id
        djt = {
            'next': self.next(),
            'previous': self.previous(),
            's': scenario,
            'show_prevnext': False,
            'correct': scenario.completed,
            'response': scenario.answer_dict[answer_id].response,
            'link_next': link_next,
        }
        self.response.out.write(webapp.template.render(path,djt))

