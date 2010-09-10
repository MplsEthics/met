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

"""Schema classes for question content."""

import yaml

_TRUE = ("true","t","y","yes","1",1)

class Scenario(yaml.YAMLObject):

    yaml_tag = '!scenario'
    name = 'foo'
    description = 'bar'

    def __init__(self,name,description):
        self.name = name
        self.description = description

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'id': self.id
        }
        return """%(class)s("%(id)s")""" % repr


class Answer(yaml.YAMLObject):

    yaml_tag = '!answer'

    checked = False
    disabled = False

    def __init__(self,_id,answer,is_correct,response):
        self.id = _id
        self.answer = answer
        self.is_correct = is_correct.lower() in _TRUE
        self.response = response

    def __repr__(self):
        repr = {
            'class': self.__class__.__name__,
            'id': self.id,
        }
        return "%(class)s(%(id)s)" % repr

