import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met.util import debug

order = [
    'main',
    'intro1',
    'intro2',
    'over1',
    'over2',
    'topic1',
    'Q1',
]


class MetView(webapp.RequestHandler):

    """
    can we initialize this webapp somehow?
    """

    view = os.path.join(os.path.dirname(__file__), '../view')

    def viewpath(self,append=None):
        if append:
            return os.path.join(self.view, './' + append)
        return self.view

    def next(self):
        pass

    def previous(self):
        pass

    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'next': self.next(),
            'previous': self.previous(),
        }

        path = self.viewpath(append='main.html')
        self.response.out.write(template.render(path, template_values))


class Main(MetView):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            #'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
        }

        path = self.viewpath(append='main.html')
        self.response.out.write(template.render(path, template_values))

class Question(webapp.RequestHandler):

#   def __init__(self,question_id):
#       self.question_id = question_id

    def get(self,question_id):
        debug()
        pass



class StaticHTML(webapp.RequestHandler):
    fn = os.path.dirname(__file__)
    def get(self):
        path = os.path.join(self.fn, '../view' + self.request.path)
        self.response.out.write(template.render(path, {}))
    post = get

