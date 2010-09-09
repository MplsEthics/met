from google.appengine.ext import webapp
from met.views.base import BaseView
from met.model import Scenario

class Content(BaseView):

    def get(self,scenario_id,view):
        template = "%s/%s.djt" % (scenario_id, view)
        path = self.viewpath(append=template)
        context = dict(next=self.next(),
                       previous=self.previous(),
                       s=Scenario.get_by_key_name(scenario_id),
                       show_prevnext=True)
        self.response.out.write(webapp.template.render(path,context))

    post = get

