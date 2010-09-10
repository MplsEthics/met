from google.appengine.ext import webapp
from met.decorators import ordered
from met.model import Answer
from met.session import LearnerState
from met.views.base import BaseView


class Response(BaseView):

    @ordered
    def get(self, scenario_id):
        state = LearnerState()
        answer_id = state.last_answer_id(scenario_id)
        response = Answer.get_by_key_name(answer_id).response
        path = self.viewpath(append='response.djt')

        if state.is_completed(scenario_id):
            link_next = "/%s/disc1" % scenario_id
        else:
            link_next = "/%s/question" % scenario_id

        context = dict(session=state.session_fmt(),
                       next=self.next(),
                       previous=self.previous(),
                       s=state,
                       show_prevnext=False,
                       correct=state.is_completed(scenario_id),
                       response=response,
                       link_next=link_next)
        output = webapp.template.render(path, context)
        self.response.out.write(output)
