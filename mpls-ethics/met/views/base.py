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

from datetime import datetime
import jinja2
import webapp2
import logging
from webapp2_extras import sessions
import met
from met.order import view_order

class BaseView(webapp2.RequestHandler):
    """Base class for all MET (Minneapolis Ethics Training) view classes."""

    def dispatch(self):
        """
        See https://webapp-improved.appspot.com/api/webapp2_extras/sessions.html
        for more on how to do sessions in webapp2.
        """
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def viewpath(self):
        """Construct a view path relative to met.app.TEMPLATE_DIR."""
        return 'main.djt'

    def view_index(self):
        request_path = self.request.path[1:]
        i = view_order.index(request_path)
        return i

    def next(self):
        """Returns the alias to the next page."""
        try:
            i = self.view_index()
            if i < len(view_order):
                return view_order[i + 1]
        except:
            return None

    def previous(self):
        """Returns the alias to the previous page."""
        try:
            i = self.view_index()
            if i > 0:
                return view_order[i - 1]
        except:
            return None

    def jinja_environment(self):
        """Return the Jinja2 environment object"""
        env = jinja2.Environment(
            loader = jinja2.FileSystemLoader(met.app.TEMPLATE_PATH),
            extensions = ['jinja2.ext.autoescape'],
            autoescape = True)

        def ordinal_day(value):
            value = value or datetime.now()
            # http://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
            dd = int(value.strftime('%-d'))
            suf = {1:"st",2:"nd",3:"rd"}.get(dd if (dd<20) else (dd%10), 'th')
            return "%d%s" % (dd, suf)

        def month_comma_year(value):
            value = value or datetime.now()
            return value.strftime('%B, %Y')

        env.filters['ordinal_day'] = ordinal_day
        env.filters['month_comma_year'] = month_comma_year
        return env

    def template(self):
        """Returns the filename of the template to view."""
        return 'main.djt'

    def get(self):
        """The default GET request handler."""
        context = {
            'next': self.next(),
            'previous': self.previous(),
            'show_prevnext': True,
        }
        jt = self.jinja_environment().get_template('main.djt')
        self.response.write(jt.render(context))

    def post(self):
        """Default POST action is to redirect to GET."""
        self.redirect(self.request.path)
