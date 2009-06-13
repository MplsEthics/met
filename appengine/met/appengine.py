from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from met.view import MainPage
from met.view import StaticHTMLPage

app_pages = [
    ('/', MainPage),
    (r'/.*\.html$', StaticHTMLPage),
#   ('/sign', Guestbook),
]

wsgi_app = webapp.WSGIApplication(app_pages,debug=True)

if __name__ == "__main__":
    run_wsgi_app(wsgi_app)

