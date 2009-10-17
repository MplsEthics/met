
from met.session import SessionMixin
import base

class Reset(base.BaseView):
    """View to reset the session hash."""

    def get(self):
        session = self.getSession()
        for key in session.keys():
            del session[key]
        self.redirect("/")

    post = get

Reset.__bases__ += (SessionMixin,)

