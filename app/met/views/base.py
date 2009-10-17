import os
import logging
from google.appengine.ext import webapp
from order import order

class BaseView(webapp.RequestHandler):
    """Base class for all MET view classes."""

    # Define a hardcoded relative path from this file to the views.  This
    # should be automated somehow!
    view_dir = os.path.join(os.path.dirname(__file__), '../../view')

    def main(self):
        """Returns the path to the 'main' view template."""
        return self.viewpath('main.djt')

    def viewpath(self,append=None):
        """Construct a view path."""
        if append:
            return os.path.join(self.view_dir, './' + append)
        return self.view_dir

    def view_index(self):
        request_path = self.request.path[1:]
        i = order.index(request_path)
        logging.info("%s => %d" % (request_path,i))
        return i

    def next(self):
        """Returns the alias to the next page."""
        try:
            i = self.view_index()
            if i < len(order):
                return order[i+1]
        except:
            return None

    def previous(self):
        """Returns the alias to the previous page."""
        try:
            i = self.view_index()
            if i > 0:
                return order[i-1]
        except:
            return None

    def template(self):
        """Returns the filename of the template to view."""
        return 'main.djt'

    def get(self):
        """The default GET request handler."""
        template_values = {
            'next': self.next(),
            'previous': self.previous(),
        }

        t = self.viewpath(append=self.template())
        self.response.out.write(webapp.template.render(t, template_values))

    def post(self):
        """Default POST action is to redirect to GET."""
        self.redirect(self.request.path)

