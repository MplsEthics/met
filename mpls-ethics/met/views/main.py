from google.appengine.ext.webapp import template
from met.views.base import SessionView
from met.session import LearnerState


class Main(SessionView):

    def get(self):
        path = self.viewpath(append='main.djt')
        state = LearnerState()
        state.update_timestamp()
        context = dict(next='instr1',
                       show_prevnext=True,
                       show_about=True,
                       session=state.session_fmt())
        self.response.out.write(template.render(path, context))
