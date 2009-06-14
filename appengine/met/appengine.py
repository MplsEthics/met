from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from met.view import Main, Question, StaticHTML

app_pages = [
    ('/', Main),
    ('/index.html', Main),
    (r'/question/.*', Question),
    (r'/.*\.html$', StaticHTML),
#   ('/sign', Guestbook),
]

wsgi_app = webapp.WSGIApplication(app_pages,debug=True)

if __name__ == "__main__":
    run_wsgi_app(wsgi_app)

