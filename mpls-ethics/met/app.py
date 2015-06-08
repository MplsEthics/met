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

import os
import webapp2
from met import views

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

app = webapp2.WSGIApplication([
    (r'^/$', views.Main),                       # splash page
    (r'^/main$', views.Main),                   # ditto
    (r'^/cookies$', views.Cookies),             # no cookie error msg
    (r'^/reset$', views.Reset),                 # clears session
    (r'^/learner$', views.Learner),             # learner form submit
    (r'^/certificate$', views.Certificate),     # learner certificate
    (r'^/cheater$', views.Cheater),             # cheater certificate
    (r'^/(\w+)/question$', views.Question),     # e.g. "coi1/question"
    (r'^/(\w+)/response$', views.Response),     # e.g. "coi1/response"
    (r'^/(\w+)/(\w+)$', views.Content),         # e.g. "coi1/intro1"
    (r'^/\w+$', views.Fallback),                # fallback / best guess
], debug=True)
