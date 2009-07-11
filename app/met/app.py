from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from met.view import Main, Scenario, BestGuess

app_pages = [
    (r'/', Main),
    (r'/scenario/(\d+)', Scenario),
    (r'/.*$', BestGuess),
]

wsgi_app = webapp.WSGIApplication(app_pages,debug=True)

if __name__ == "__main__":
    run_wsgi_app(wsgi_app)

