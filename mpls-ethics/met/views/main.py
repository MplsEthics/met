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

from google.appengine.ext.webapp import template
from met.views.base import BaseView
from met.session import LearnerState


class Main(BaseView):

    def get(self):
        path = self.viewpath(append='main.djt')
        state = LearnerState()
        state.update_timestamp()
        context = dict(next='instr1',
                       show_prevnext=True,
                       show_about=True,
                       state=state.as_string())
        self.response.out.write(template.render(path, context))
