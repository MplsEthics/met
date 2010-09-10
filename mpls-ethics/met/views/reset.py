from met.views.base import BaseView
from met.session import LearnerState

class Reset(BaseView):
    """Clear the session."""

    def get(self):
        LearnerState().flush_session()
        self.redirect("/")
