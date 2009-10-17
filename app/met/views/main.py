import os
import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met import content
from met import session

import base

class Main(base.BaseView):
    def get(self):
        path = self.viewpath(append='main.djt')
        session = self.getSession()
        try:
            session['timestamp'] += [ datetime.now() ]
        except:
            session['timestamp'] = []
        session['timestamp'] = session['timestamp'][0:3]
        next = 'instr1'
        logging.info(locals())
        self.response.out.write(template.render(path,locals()))

    post = get

Main.__bases__ += (session.SessionMixin,)

