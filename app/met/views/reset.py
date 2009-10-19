
import base
from met import session

class Reset(base.BaseView, session.SessionMixin):
    """View to reset the session hash."""

    def get(self):
        self.getSession().flush()
        self.redirect("/")

