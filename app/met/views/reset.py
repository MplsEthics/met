
import base
from met import session

class Reset(base.BaseView, session.SessionMixin):
    """View to reset the session hash."""

    def get(self):
        session = self.getSession()
        for key in session.keys():
            del session[key]
        self.redirect("/")

