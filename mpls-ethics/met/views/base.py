import os
from google.appengine.ext import webapp
from met.order import scenario_order, view_order
from met.session import Session

class BaseView(webapp.RequestHandler):
    """Base class for all MET (Minneapolis Ethics Training) view classes."""

    # Define a hardcoded relative path from this file to the views.  This
    # should be automated somehow!
    view_dir = os.path.join(os.path.dirname(__file__), '../../view')

    def main(self):
        """Returns the path to the 'main' view template."""
        return self.viewpath('main.djt')

    def viewpath(self,append=None):
        """Construct a view path."""
        if append:
            return os.path.join(self.view_dir, './' + append)
        return self.view_dir

    def view_index(self):
        request_path = self.request.path[1:]
        i = view_order.index(request_path)
        return i

    def next(self):
        """Returns the alias to the next page."""
        try:
            i = self.view_index()
            if i < len(view_order):
                return view_order[i+1]
        except:
            return None

    def previous(self):
        """Returns the alias to the previous page."""
        try:
            i = self.view_index()
            if i > 0:
                return view_order[i-1]
        except:
            return None

    def template(self):
        """Returns the filename of the template to view."""
        return 'main.djt'

    def get(self):
        """The default GET request handler."""
        template_values = {
            'next': self.next(),
            'previous': self.previous(),
            'show_prevnext': True,
        }

        t = self.viewpath(append=self.template())
        self.response.out.write(webapp.template.render(t, template_values))

    def post(self):
        """Default POST action is to redirect to GET."""
        self.redirect(self.request.path)


class SessionView(BaseView):
    """Just like BaseView, with the addition of method get_session(), which
    allows access to the session."""

    def get_session(self):
        """Cache and return an initialized session object."""
        if getattr(self,'_session',None) is None:
            self._session = Session()
        return self._session


class SecureView(SessionView):
    """This view class extends the session view with features for ensuring
    that learners are not accessing views out of order."""

    def assert_all_scenarios_completed(self):
        if not self.all_scenarios_completed():
            incomplete = self.first_incomplete_scenario()
            self.redirect("/%s/intro1" % incomplete)

    def assert_scenario_order(self,scenario_id):
        """If the learner is trying to access this scenario out of order,
        redirect to the first incomplete scenario."""
        # FIXME: do I need compdict?
        compdict = self.get_session()['completed']
        if not self.prereqs_completed(scenario_id):
            incomplete = self.first_incomplete_scenario()
            self.redirect("/%s/intro1" % incomplete)

    def prereqs_completed(self,scenario_id):
        """Returns True if all the scenarios before to 'scenario_id' have been
        completed, as indicated by their status in 'compdict'.  Returns False
        otherwise.  This function can be used to determine if the user is
        trying to complete the scenarios out of order."""
        compdict = self.get_session()["completed"]
        assert scenario_id in scenario_order, 'test scenario must be known'
        k = scenario_order.index(scenario_id)
        for sid in scenario_order[0:k]:
            if sid not in compdict:
                return False
        return True

    def all_scenarios_completed(self):
        """Returns True if all the scenarios are in the dict that records
        scenario completiions ('compdict').  Returns False otherwise."""
        compdict = self.get_session()["completed"]
        for sid in scenario_order:
            if sid not in compdict:
                return False
        return True

    def first_incomplete_scenario(self):
        compdict = self.get_session()["completed"]
        for sid in scenario_order:
            if sid not in compdict:
                return sid
        return None

