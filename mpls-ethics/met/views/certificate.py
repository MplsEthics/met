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

from datetime import datetime
from met.decorators import alldone
from met.views.base import BaseView
from met.state import LearnerState
from met.version import VERSION


class Certificate(BaseView):
    """View class for the certificate."""

    @alldone
    def get(self, *argv):
        state = LearnerState(self.session)
        context = dict(show_prevnext=False,
                       version=VERSION,
                       now=datetime.now(),
                       state=state.as_string(),
                       learner_name=state.learner_name(),
                       learner_board=state.learner_board(),
                       learner_date=state.learner_date())
        jt = self.jinja_environment().get_template('certificate.djt')
        self.response.write(jt.render(context))
