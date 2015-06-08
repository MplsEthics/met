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
from met.state import LearnerState


class Cookies(BaseView):
    """
    Page view to validate that cookies are enabled.  Here's how it works:
        1. if the main page doesn't see the special "_mplsethics" cookie, it
           attempts to set the cookie, and redirects to this page.
        2. if this page doesn't see the cookie, then we know the cookie didn't
           take, so we show an error message.
        3. if this page *does* see the cookie, we know the cookie did take, so
           we can safely redirect back to the main page (which should then not
           redirect back here, as it should still see the cookie).
    """

    def get(self):
        state = LearnerState(self.session)
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

        jt = self.jinja_environment().get_template('cookies.djt')
        self.response.write(jt.render(context))
