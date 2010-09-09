from google.appengine.ext import webapp
from met.views.base import BaseView
from met.exceptions import InvalidScenarioException
from met.model import Scenario


class Content(BaseView):
    """Shows any page containing scenario content."""

    def get(self, scenario_id, view):
        template = "%s/%s.djt" % (scenario_id, view)
        path = self.viewpath(append=template)
        scenario = Scenario.get_by_key_name(scenario_id)
        if not scenario:
            raise InvalidScenarioException('bad scenario ID')

        context = dict(next=self.next(),
                       previous=self.previous(),
                       s=scenario.as_dict(),
                       show_prevnext=True)
        self.response.out.write(webapp.template.render(path, context))

    post = get
