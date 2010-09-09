from met.views.base import SessionView

class Reset(SessionView):
    """View to reset the session hash."""

    def get(self):
        self.get_session().flush()
        self.redirect("/")
