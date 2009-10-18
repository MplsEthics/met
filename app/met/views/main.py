import logging
from datetime import datetime
from google.appengine.ext.webapp import template
from met import session
import base

class Main(base.BaseView, session.SessionMixin):
    def get(self):
        path = self.viewpath(append='main.djt')
        session = self.getSession()
        try:
            session['timestamp'] += [ datetime.now() ]
        except:
            session['timestamp'] = [ datetime.now() ]
        session['timestamp'] = session['timestamp'][0:3]
        next = 'instr1'
        show_prevnext = True
        logging.info(locals())
        self.response.out.write(template.render(path,locals()))

