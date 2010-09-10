# Copyright 2010 John J. Trammell.
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
from met.views.base import BaseView
from google.appengine.ext import webapp
from met.session import LearnerState
from met.version import VERSION


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
                       state=state.as_string(),
                       version=VERSION,
                       show_prevnext=True)
        self.response.out.write(webapp.template.render(path, context))

    post = get
