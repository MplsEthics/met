import os
from met.views.base import BaseView
from google.appengine.ext import webapp
from met.session import LearnerState


class Fallback(BaseView):
    """View class that displays the view closest to that requested."""

    def template(self):
        """Return the view template that best matches the request."""

        # if the path is impossibly short, show the main template
        if len(self.request.path) <= 1:
            return 'main.djt'

        # if view_dir + self.request.path + ".djt" is a view, then use it
        srp = self.request.path[1:] + ".djt"
        if os.path.exists(self.viewpath(append=srp)):
            return srp

        # try to find a matching
        if len(self.request.path) > 1:
            templates = [x for x in os.listdir(self.view_dir) if x[0] != '.']
            for t in templates:
                if self.request.path[1:] in t:
                    return t

        # sane fallback
        return 'main.djt'

    def get(self, *argv):
        path = self.viewpath(append=self.template())
        state = LearnerState()
        context = dict(previous=self.previous(),
                       next=self.next(),
                       session=state.session_fmt(),
                       show_prevnext=True)
        self.response.out.write(webapp.template.render(path, context))

    post = get
