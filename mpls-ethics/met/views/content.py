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
                       state=state.as_string(),
                       show_prevnext=True)
        self.response.out.write(webapp.template.render(path, context))

    post = get
