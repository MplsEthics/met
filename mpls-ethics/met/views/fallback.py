# Copyright 2015 John J. Trammell.
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
import met
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

        # if the request path corresponds to a template, then show it
        srp = self.request.path[1:] + ".djt"
        if os.path.exists(os.path.join(met.app.TEMPLATE_PATH, srp)):
            return srp

        # sane fallback
        return 'main.djt'

    def get(self, *argv):
        state = LearnerState()
        context = dict(previous=self.previous(),
                       next=self.next(),
                       state=state.as_string(),
                       version=VERSION,
                       show_prevnext=True)
        jt = self.jinja_environment().get_template(self.template())
        self.response.write(jt.render(context))

    post = get
