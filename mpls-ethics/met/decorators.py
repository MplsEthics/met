"""
"""

from met.session import LearnerState


class Ordered(object):
    """If the learner is trying to access the questions out of order, redirect
    to the first incomplete scenario."""

    def __init__(self, f):
        self.func = f

    def __call__(self, scenario_id, *argv, **kwargs):
        # if the prerequisites for this scenario have been completed, then
        # display the view, otherwise redirect to the start of the first
        # incomplete scenario
        state = LearnerState()
        if state.completed_prerequisites(scenario_id):
            return self.func(scenario_id, *argv, **kwargs)
        else:
            scenario_id = state.first_incomplete_scenario()
            self.redirect("/%s/intro1" % scenario_id)
            return
