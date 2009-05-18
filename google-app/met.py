import os
import cgi
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

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

        path = os.path.join(os.path.dirname(__file__), 'djt/splash.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        self.redirect('/instructions.html')

application = webapp.WSGIApplication(
    [
        ('/', MainPage),
#       ('/sign', Guestbook),
    ],
    debug=True,
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

