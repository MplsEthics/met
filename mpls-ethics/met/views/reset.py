import base

class Reset(base.SessionView):
    """View to reset the session hash."""

    def get(self):
        self.getSession().flush()
        self.redirect("/")

