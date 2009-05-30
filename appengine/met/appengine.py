import os
import cgi
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

def debug():
    import sys
    import pdb
    for attr in ('stdin', 'stdout', 'stderr'):
        setattr(sys, attr, getattr(sys, '__%s__' % attr))
    pdb.set_trace()

class MainPage(webapp.RequestHandler):
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

        path = os.path.join(os.path.dirname(__file__), '../djt/main.html')
        self.response.out.write(template.render(path, template_values))

class StaticHTMLPage(webapp.RequestHandler):
    fn = os.path.dirname(__file__)
    def get(self):
        path = os.path.join(self.fn, '..' + self.request.path)
        self.response.out.write(template.render(path, {}))
    post = get

app_pages = [
    ('/', MainPage),
    (r'/.*\.html$', StaticHTMLPage),
#   ('/sign', Guestbook),
]

wsgi_app = webapp.WSGIApplication(app_pages,debug=True)

def main():
    run_wsgi_app(wsgi_app)

if __name__ == "__main__":
    main()

