"""
"""

from met.session import LearnerState


def ordered(func):
    """If the learner is trying to access the questions out of order, redirect
    to the first incomplete scenario."""

    def wrapper(self, scenario_id, *args, **kwargs):
        """
        If the prerequisites for this scenario have been completed, then
        display the view, otherwise redirect to the start of the first
        incomplete scenario.
        """
        state = LearnerState()
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
        state = LearnerState()
        if state.completed_all():
            return func(self, *args, **kwargs)
        else:
            scenario_id = state.first_incomplete_scenario()
            self.redirect("/%s/intro1" % scenario_id)
            return

    return wrapper
