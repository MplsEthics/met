# Copyright 2015 John J. Trammell.
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

from met.state import LearnerState


def ordered(func):
    """If the learner is trying to access the questions out of order, redirect
    to the first incomplete scenario."""

    def wrapper(self, scenario_id, *args, **kwargs):
        """
        If the prerequisites for this scenario have been completed, then
        display the view, otherwise redirect to the start of the first
        incomplete scenario.
        """
        state = LearnerState(self.session)
        if state.completed_prerequisites(scenario_id):
            return func(self, scenario_id, *args, **kwargs)
        else:
            scenario_id = state.first_incomplete_scenario()
            self.redirect("/%s/intro1" % scenario_id)
            return

    return wrapper


def alldone(func):
    """If the learner is trying to access a view before having completed all
    scenarios, redirect to the first incomplete scenario."""

    def wrapper(self, *args, **kwargs):
        """
        If the prerequisites for this scenario have been completed, then
        display the view, otherwise redirect to the start of the first
        incomplete scenario.
        """
        state = LearnerState(self.session)
        if state.completed_all():
            return func(self, *args, **kwargs)
        else:
            scenario_id = state.first_incomplete_scenario()
            self.redirect("/%s/intro1" % scenario_id)
            return

    return wrapper
