from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from met.views import Main, Reset, Scenario, Fallback

app_pages = [
    (r'^/$', Main),                 # splash page
    (r'^/main$', Main),             # ditto
    (r'^/reset$', Reset),           # clears session
    (r'^/(\w+)/(\w+)$', Scenario),  # e.g. "coi1/intro"
    (r'^/\w+$', Fallback),          # best guess
]

wsgi_app = webapp.WSGIApplication(app_pages,debug=True)

if __name__ == "__main__":
    run_wsgi_app(wsgi_app)

