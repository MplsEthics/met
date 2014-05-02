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


from google.appengine.ext import db
from met.model import Board

def boards():
    """
    Returns a list of the City of Minneapolis boards & commissions, taken
    mostly from URL http://www.ci.minneapolis.mn.us/boards-and-commissions/.
    Internal datastore uses integer ID for clean sorting.
    """
    gql = db.GqlQuery("SELECT * FROM Board ORDER BY __key__");
    return gql.fetch(limit=100)
