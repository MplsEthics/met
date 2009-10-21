from google.appengine.ext import webapp
import base
from met import content

class Content(base.BaseView):

    def get(self,scenario_id,view):
        a = "%s/%s.djt" % (scenario_id, view)
        path = self.viewpath(append=a)
        djt = {
            'next': self.next(),
            'previous': self.previous(),
            's': content.get_scenario(scenario_id),
            'show_prevnext': True,
        }
        self.response.out.write(webapp.template.render(path,djt))

    post = get

