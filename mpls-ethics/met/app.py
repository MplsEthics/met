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
from google.appengine.ext.webapp.util import run_wsgi_app
from met import views

app_pages = [
    (r'^/$', views.Main),                       # splash page
    (r'^/main$', views.Main),                   # ditto
    (r'^/reset$', views.Reset),                 # clears session
    (r'^/learner$', views.Learner),             # learner form submit
    (r'^/certificate$', views.Certificate),     # learner certificate
    (r'^/cheater$', views.Cheater),             # cheater certificate
    (r'^/(\w+)/question$', views.Question),     # e.g. "coi1/question"
    (r'^/(\w+)/response$', views.Response),     # e.g. "coi1/response"
    (r'^/(\w+)/(\w+)$', views.Content),         # e.g. "coi1/intro1"
    (r'^/\w+$', views.Fallback),                # fallback / best guess
]

wsgi_app = webapp.WSGIApplication(app_pages, debug=True)

if __name__ == "__main__":
    run_wsgi_app(wsgi_app)
