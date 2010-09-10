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

from datetime import datetime
from google.appengine.ext import webapp
from met.decorators import alldone
from met.views.base import BaseView
from met.session import LearnerState
from met.version import VERSION


class Certificate(BaseView):
    """View class for the certificate."""

    @alldone
    def get(self, *argv):
        path = self.viewpath(append='certificate.djt')
        state = LearnerState()
        context = dict(show_prevnext=False,
                       version=VERSION,
                       now=datetime.now(),
                       state=state.as_string(),
                       learner_name=state.learner_name(),
                       learner_board=state.learner_board())
        output = webapp.template.render(path, context)
        self.response.out.write(output)
