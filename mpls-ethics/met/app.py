from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from met import views

app_pages = [
    (r'^/$', views.Main),                       # splash page
    (r'^/main$', views.Main),                   # ditto
    (r'^/reset$', views.Reset),                 # clears session
    (r'^/learner$', views.Learner),             # learner form submit
    (r'^/certificate$', views.Certificate),     # learner certificate
    (r'^/cheater$', views.Cheater),             # cheater certificate
    (r'^/(\w+)/question$', views.Question),     # e.g. "coi1/question"
    (r'^/(\w+)/response$', views.Response),     # e.g. "coi1/response"
    (r'^/(\w+)/(\w+)$', views.Content),         # e.g. "coi1/intro1"
    (r'^/\w+$', views.Fallback),                # fallback / best guess
]

wsgi_app = webapp.WSGIApplication(app_pages, debug=True)

if __name__ == "__main__":
    run_wsgi_app(wsgi_app)
