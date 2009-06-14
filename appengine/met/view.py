import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from met.util import debug

viewpath = os.path.join(os.path.dirname(__file__),'../view')

class Main(webapp.RequestHandler):
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

        path = viewpath + '/main.html'
        self.response.out.write(template.render(path, template_values))

class Question(webapp.RequestHandler):


    def get(self):
        debug()
        pass




class StaticHTML(webapp.RequestHandler):
    fn = os.path.dirname(__file__)
    def get(self):
        path = os.path.join(self.fn, '../view' + self.request.path)
        self.response.out.write(template.render(path, {}))
    post = get

