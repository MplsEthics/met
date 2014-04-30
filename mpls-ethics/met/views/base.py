# Copyright 2012 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics
# is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

import os
from google.appengine.ext import webapp


class BaseView(webapp.RequestHandler):
    """
    Base class for all MET (Minneapolis Ethics Training) view classes.
    """

    # Define a hardcoded relative path from this file to the views.  This
    # should be automated somehow!
    view_dir = os.path.join(os.path.dirname(__file__), '../../view')

    def main(self):
        """Returns the path to the 'main' view template."""
        return self.viewpath('main.djt')

    def viewpath(self, append=None):
        """Construct a view path."""
        if append:
            return os.path.join(self.view_dir, './' + append)
        return self.view_dir

    def request_path(self):
        """
        Return the path of the current request, minus any leading slash.
        """
        return self.request.path[1:]

    def view_index(self):
        """
        Return the (integer) index of the current request path.
        """
        return db.GqlQuery("SELECT order FROM View WHERE view=:1",
            self.request_path()).get()

    def next(self):
        """
        Returns the alias to the next page, None if there is no next page.
        """
        return db.GqlQuery("SELECT view FROM View WHERE order=:1",
            self.view_index() + 1).get()

    def previous(self):
        """
        Returns the alias to the previous page, None if there is no previous
        page.
        """
        return db.GqlQuery("SELECT view FROM View WHERE order=:1",
            self.view_index() - 1).get()

    def template(self):
        """
        Returns the filename of the template to view.  This should be
        overridden in any subclass...
        """
        return 'main.djt'

    def get(self):
        """
        The default GET request handler.
        """
        template_values = {
            'next': self.next(),
            'previous': self.previous(),
            'show_prevnext': True,
        }
        t = self.viewpath(append=self.template())
        self.response.out.write(webapp.template.render(t, template_values))

    def post(self):
        """
        Default POST action is to redirect to GET.
        """
        self.redirect(self.request.path)
