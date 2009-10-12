import os
import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met import content
from met import session

# define the navigation view order
order = [
    'main',
    'instr1',
    'instr2',
    'over1',
    'over2',

    # intrduce topic 1: conflict of interest
    'topic1',

    # conflict of interest part 1
    'coi1/intro',
    'coi1/scenario',
    'coi1/disc1',
    'coi1/disc2',

    # conflict of interest part 2
    'coi2/intro',
    'coi2/scenario',
    'coi2/disc1',
    'coi2/disc2',
    'coi2/disc3',

    # conflict of interest part 3
    'coi3/intro',
    'coi3/scenario',
    'coi3/disc1',
    'coi3/disc2',
    'coi3/disc3',

    # conflict of interest part 4
    'coi4/intro',
    'coi4/scenario',
    'coi4/disc1',

    # disclosure of information
    'doi/intro',
    'doi/scenario',
    'doi/disc1',

    # gifts
    'gifts/intro1',
    'gifts/intro2',
    'gifts/scenario',
    'gifts/disc1',

    # ethics report line & contact info
    'reportline1',
    'reportline2',
    'reportline3',

    'contacts',
    'congrats',
    'certificate',
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

    def view_index(self):
        srp = self.request.path[1:]
        i = order.index(srp)
        logging.info("%s => %d" % (srp,i))
        return i

    def next(self):
        """Returns the alias to the next page."""
        try:
            i = self.view_index()
            if i < len(order):
                return order[i+1]
        except:
            return None

    def previous(self):
        """Returns the alias to the previous page."""
        try:
            i = self.view_index()
            if i > 0:
                return order[i-1]
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
        }

        t = self.viewpath(append=self.template())
        self.response.out.write(template.render(t, template_values))

class Main(MetView):
    def get(self):
        path = self.viewpath(append='main.djt')
        session = self.getSession()
        try:
            session['timestamp'] += [ datetime.now() ]
        except:
            session['timestamp'] = []
        session['timestamp'] = session['timestamp'][0:3]
        next = 'instr1'
        logging.info(locals())
        self.response.out.write(template.render(path,locals()))

    post = get

Main.__bases__ += (session.SessionMixin,)


class BestGuess(MetView):
    """View class that displays the view closest to that requested."""

    def get(self, *argv):
        logging.info(argv)
        path = self.viewpath(append=self.template())
        previous = self.previous()
        next = self.next()
        self.response.out.write(template.render(path,locals()))

    def template(self):
        """Return the view template that best matches the request."""

        # if view_dir + self.request.path + ".djt" is a view, then use it
        srp = self.request.path[1:] + ".djt"
        if os.path.exists(self.viewpath(append=srp)):
            return srp

        if len(self.request.path) <= 1:
            return 'main.djt'
        if len(self.request.path) > 1:
            for t in self.list_templates():
                if self.request.path[1:] in t:
                    return t
            return 'main.djt'

    def list_templates(self):
        t = os.listdir(self.view_dir)
        t = [ x for x in t if x[0] != '.' ]
        return t

    post = get


class Scenario(MetView):

    def get(self,scenario_id,view):
        if view != 'scenario':
            a = "%s/%s.djt" % (scenario_id, view)
            path = self.viewpath(append=a)
            djt = {
                'next': self.next(),
                'previous': self.previous(),
                's': content.get_scenario(scenario_id),
            }
            self.response.out.write(template.render(path,djt))
        else:
            self.get_scenario(scenario_id)

    def get_scenario(self,scenario_id):
        scenario = content.get_scenario(scenario_id)
        session = self.getSession()
        path = self.viewpath(append='scenario.djt')
        if scenario_id in session:
            last_answer = session[scenario_id][-1]
        scenario.is_correct(last_answer)
        djt = {
            'previous': self.previous(),
            'next': self.next(),
            's': scenario,
            'session': session,
            'is_correct': scenario.is_correct(last_answer),
        }
        self.response.out.write(template.render(path,djt))

    def post(self,scenario_id,view):
        """Process the answer submission, then redirect to the question
        view."""
        scenario = content.get_scenario(scenario_id)
        session = self.getSession()
        answer = self.request.params['answer']
        if scenario_id in session:
            session[scenario_id] += [ answer ]
        else:
            session[scenario_id] = [ answer ]
        self.redirect("/%s/scenario" % scenario_id)

Scenario.__bases__ += (session.SessionMixin,)

