======================
Ethics Training Webapp
======================
.. footer::
    John Trammell *<johntrammell@gmail.com>*

With the Google App Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: appengine_lowres.gif
    :align: center

|
| John Trammell, Fall 2009



Minneapolis Ethics Training
---------------------------
.. class:: incremental

- three recent felony ethics lapses
- Ethics Officer
- face-to-face training



Minneapolis Ethics Training
---------------------------
.. class:: incremental

- custom computerized training
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
.. image:: skiing.jpg
    :align: right

.. class:: incremental

- desktop app
- "Scheme on Skis"
- Perl + Catalyst
- Python + ???
- *Google App Engine!*



Development
-----------
.. class:: incremental

- github



App Engine 101
--------------
.. class:: incremental

- free (up to storage, CPU, bandwidth quotas)
- build locally using SDK
- upload to Google (``appspot.com``)
- uses Google infrastructure for scaling
- supports apps in Java, Python (2.5)
- use the 'webapp' framework
- a few 3rd-party libraries (PyCrypto, PyYAML, zipimport, ...)



App Engine 102
--------------
.. class:: incremental

- persistent OO storage
- email send/receive
- scheduled tasks / task queues
- some image transforms



The *mpls-ethics* Web App
---------------------------
.. class:: incremental

- linear progression through scenarios
    - text
    - multiple-choice questions
- persist answers to questions
- email completion status



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
        # ... pages removed for clarity ...
    ]
    wsgi_app = webapp.WSGIApplication(app_pages,debug=True)
    if __name__ == "__main__":
        run_wsgi_app(wsgi_app)


View Class
----------





Django Templates
----------------





Browser Sessions
----------------
.. class:: incremental

- browser sessions via 3rd-party  ``gaeutilities``
- needed a little coaxing
- but I got it to work



Completion Tracking - email
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



Completion Tracking - storage
-----------------------------
Use GAE storage model::

    from google.appengine.ext import db
    class Completion(db.Model):
        name = db.StringProperty(
            verbose_name='Learner Name')
        board = db.StringProperty(
            verbose_name='Learner Board or Commission')
        date = db.DateTimeProperty(
            verbose_name='Completion Timestamp',
            auto_now_add=True)



Completion Tracking - storage
-----------------------------
::

    from met.model import Completion
    comp = Completion()
    comp.name = learner_name
    comp.board = learner_board
    comp.put()



About this talk
---------------

* source is in Restructured Text
* uses rst2s5.py to generate S5 XHTML

