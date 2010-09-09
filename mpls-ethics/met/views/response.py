from google.appengine.ext import webapp
from met.session import LearnerState
from met.model import Answer
from met.views.base import SessionView


class Response(SessionView):

    def get(self, scenario_id):
        session = self.get_session()
        state = LearnerState()
        answer_id = self.last_answer_id(scenario_id)
        answer = Answer.get_by_key_name(answer_id)
        path = self.viewpath(append='response.djt')
        if state.is_completed(scenario_id):
            link_next = "/%s/disc1" % scenario_id
        else:
            link_next = "/%s/question" % scenario_id
        context = dict(session=session,
                       next=self.next(),
                       previous=self.previous(),
                       s=state,
                       show_prevnext=False,
                       correct=state.is_completed(),
                       response=answer.response,
                       link_next=link_next)
        output = webapp.template.render(path, context)
        self.response.out.write(output)

    def last_answer_id(self, scenario_id):
        try:
            return self.get_session()[scenario_id][-1]
        except:
            return None

    def learner_response(self, scenario, answer_id):
        """Returns a string containing the response we want to give to the
        learner."""
        answer = scenario.answer_dict.get(answer_id, "")
        if answer is not None:
            return answer.response
        else:
            return None
