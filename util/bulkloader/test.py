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

from met.model import Scenario
from pprint import pprint

pprint([x for x in  Scenario.all()])
s = Scenario.all()[0]
pprint(s.__dict__)
pprint(dir(s))
pprint(s.fields())

# try get_by_key_name
s = Scenario.get_by_key_name('coi1')
pprint(s.__dict__)

# how does it fail?
s = Scenario.get_by_key_name('coi99')
pprint(s.__dict__)

# test the answer_set attribute
s = Scenario.get_by_key_name('coi1')
from pprint import pprint
pprint([x.__dict__ for x in s.answer_set])
