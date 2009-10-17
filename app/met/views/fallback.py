import os
import logging
import base
from google.appengine.ext import webapp

class Fallback(base.BaseView):
    """View class that displays the view closest to that requested."""

    def get(self, *argv):
        logging.info(argv)
        path = self.viewpath(append=self.template())
        previous = self.previous()
        next = self.next()
        self.response.out.write(webapp.template.render(path,locals()))

    def template(self):
        """Return the view template that best matches the request."""

        # if view_dir + self.request.path + ".djt" is a view, then use it
        srp = self.request.path[1:] + ".djt"
        if os.path.exists(self.viewpath(append=srp)):
            return srp

        if len(self.request.path) <= 1:
            return 'main.djt'
        if len(self.request.path) > 1:
            for t in self.list_templates():
                if self.request.path[1:] in t:
                    return t
            return 'main.djt'

    def list_templates(self):
        t = os.listdir(self.view_dir)
        t = [ x for x in t if x[0] != '.' ]
        return t

    post = get

