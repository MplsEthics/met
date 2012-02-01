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

import logging
from google.appengine.ext.webapp import template
from met.views.base import BaseView
from met.session import LearnerState


class Cookies(BaseView):
    """Page view to  """

    def get(self):
        path = self.viewpath(append='cookies.djt')
        state = LearnerState()
        state.update_timestamp()

        # if the test cookie is set, we know that this user has cookies
        # enabled, so redirect back to the main page
        if '_mplsethics' in self.request.cookies:
            logging.info('hooray, cookies are enabled')
            self.redirect('/main')
            return
        else:
            logging.info('bummer, cookies are disabled')
            logging.info('%s', self.request.cookies.keys())

        # otherwise tell the user to turn cookies on...
        context = dict(next='main',
                       show_prevnext=True,
                       state=state.as_string())
        self.response.out.write(template.render(path, context))
