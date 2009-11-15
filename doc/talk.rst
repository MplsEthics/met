======================
Ethics Training Webapp
======================
.. footer:: John Trammell *<johntrammell@gmail.com>*

With the Google App Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: appengine_lowres.gif
    :align: center

Minneapolis Ethics Training
---------------------------
.. class:: incremental

- various ethics lapses
- Ethics Officer
- face-to-face training
- training
    - modeled training off of DOD web app

Requirements
------------
.. class:: incremental

- "distribute" app to trainees
- learners progress through three topics
    - conflict of interest
    - disclosure of information
    - gifts
- completion information collected... somehow
- certificate of completion


Language, Platform, and Hosting
-------------------------------
.. class:: incremental

- desktop app
- "Scheme on Skis"
- Perl + Catalyst
- Python + ???
- *Google App Engine!*


A Simple Web App
----------------
.. class:: incremental

* progress through scenarios
* persist status
* email completion status


App Configuration
-----------------

::

    application: 'mpls-ethics'
    runtime: python
    handlers:
    - url: /images
      static_dir: static/images
    - url: /css
      static_dir: static/css
    - url: /.*
      script: met/app.py


App Dispatcher
--------------

::

    from google.appengine.ext import webapp
    from google.appengine.ext.webapp.util import run_wsgi_app
    from met import views
    app_pages = [
        (r'^/$', views.Main),
        (r'^/(\w+)/response$', views.Response),
        (r'^/(\w+)/(\w+)$', views.Content),
        # ... pages removed for clarity ...
    ]
    wsgi_app = webapp.WSGIApplication(app_pages,debug=True)
    if __name__ == "__main__":
        run_wsgi_app(wsgi_app)



Question Data
-------------
- ``JSON``?
- ``YAML``?

PyYAML is provided by GAE!


Persistence
-----------
.. class:: incremental

- sessions via ``gaeutilities``
- needs a little coaxing
- but it can be made to work

Completion Tracking, Part 1
---------------------------
GAE has an 'email' API::

    from google.appengine.api import mail
    def send_completion(learner):
        msg = mail.EmailMessage()
        msg.sender = 'ethics@example.com'
        msg.to = 'training@example.com'
        msg.subject = "Ethics training completion"
        msg.body = """ ... """ % learner
        msg.send()

Completion Tracking, Part 2
---------------------------
Use GAE storage::

    # define storage class
    # stash the data

About this talk
---------------

* source is in Restructured Text
* uses rst2s5.py to generate S5 XHTML

