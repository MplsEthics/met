import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met import util
from met import content

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

    def main(self):
        return self.viewpath('main.djt')

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
        path = self.viewpath(append='main.djt')
        self.response.out.write(template.render(path,{}))

class BestGuess(MetView):
    def templates(self):
        return sorted(os.listdir(self.view))

    def get(self):
        path = self.viewpath(append='main.djt')

        for t in self.templates():
            if self.request.path[1:] in t:
                path = self.viewpath(append=t)
                break

        self.response.out.write(template.render(path,{}))

    post = get

class Scenario(MetView):

#   def __init__(self,question_id):
#       self.question_id = question_id

    def get(self,qid):
        question_id = int(qid)
        path = self.viewpath(append='question.djt')
        #util.debug()
        template_values = {
            'question': content.get_question(question_id),
        }
        self.response.out.write(template.render(path, template_values))

    def post(self,_question_id):
        pass

class StaticHTML(webapp.RequestHandler):
    fn = os.path.dirname(__file__)
    def get(self):
        path = os.path.join(self.fn, '../view' + self.request.path)
        self.response.out.write(template.render(path, {}))
    post = get

