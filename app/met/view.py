import os
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met import util
from met import content
from met import session

order = [
    'main',
    'intro1',
    'intro2',
    'over1',
    'over2',
    'topic1',
    'scenario/coi1',    # conflict of interest 1
    'scenario/coi2',    # conflict of interest 2
    'scenario/coi3',    # conflict of interest 3
    'scenario/coi4',    # conflict of interest 4
    'scenario/doi',     # disclosure of information
    'scenario/gifts',
    'reportline',
    'summary',
]

class MetView(webapp.RequestHandler):
    """Base class for all MET view classes."""

    view_dir = os.path.join(os.path.dirname(__file__), '../view')

    def main(self):
        """Returns the path to the 'main' view template."""
        return self.viewpath('main.djt')

    def viewpath(self,append=None):
        """Construct a view path."""
        if append:
            return os.path.join(self.view_dir, './' + append)
        return self.view_dir

    def next(self):
        """Returns the alias to the next page."""
        pass

    def previous(self):
        """Returns the alias to the previous page."""
        pass

    def template(self):
        """Returns the filename of the template to view."""
        return 'main.djt'

    def get(self):
        """The default GET request handler."""
        template_values = {
            'next': self.next(),
            'previous': self.previous(),
        }

        t = self.viewpath(append=self.template())
        self.response.out.write(template.render(t, template_values))

class Main(MetView):
    def get(self):
        path = self.viewpath(append='main.djt')
        session = self.getSession()
        session['timestamp'] = datetime.now()
        self.response.out.write(template.render(path,locals()))

    post = get

Main.__bases__ += (session.SessionMixin,)


class BestGuess(MetView):
    """View class that displays the view closest to that requested."""

    def get(self):
        path = self.viewpath(append=self.template())
        self.response.out.write(template.render(path,{}))

    def template(self):
        """Return the view template that best matches the request."""
        if len(self.request.path) <= 1:
            return 'main.djt'
        if len(self.request.path) > 1:
            for t in sorted(os.listdir(self.view_dir)):
                if self.request.path[1:] in t:
                    return t
            return 'main.djt'

    post = get



class Scenario(MetView):

    def __init__(self,question_id):
        self.question_id = question_id

    def get(self,qid):
        question_id = int(qid)
        path = self.viewpath(append='question.djt')
        #util.debug()
        template_values = {
            'question': content.get_question(question_id),
        }
        self.response.out.write(template.render(path, template_values))

    def post(self,question_id):
        pass

Scenario.__bases__ += (session.SessionMixin,)

