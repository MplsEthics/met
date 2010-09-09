from google.appengine.ext import webapp
import base
from met import content

class Response(base.SessionView):

    def get(self,scenario_id):
        session = self.getSession()
        scenario = content.merge_scenario(scenario_id,session)
        answer_id = self.last_answer_id(scenario_id)
        path = self.viewpath(append='response.djt')
        if scenario.completed:
            link_next = "/%s/disc1" % scenario_id
        else:
            link_next = "/%s/question" % scenario_id
        djt = {
            'next': self.next(),
            'previous': self.previous(),
            's': scenario,
            'show_prevnext': False,
            'correct': scenario.completed,
            'response': self.learner_response(scenario,answer_id),
            'link_next': link_next,
        }
        self.response.out.write(webapp.template.render(path,djt))

    def last_answer_id(self,scenario_id):
        try:
            return self.getSession()[scenario_id][-1]
        except:
            return None

    def learner_response(self,scenario,answer_id):
        """Returns a string containing the response we want to give to the
        learner."""
        answer = scenario.answer_dict.get(answer_id,None)
        if answer is not None:
            return answer.response
        else:
            return None
