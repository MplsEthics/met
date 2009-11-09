import logging
from datetime import datetime
from google.appengine.ext.webapp import template
import base

class Main(base.SessionView):
    def get(self):
        path = self.viewpath(append='main.djt')
        session = self.getSession()
        timestamps = session.get('timestamp',[])
        timestamps.append(datetime.now().isoformat())
        session['timestamp'] = timestamps[0:3]
        next = 'instr1'
        show_prevnext = True
        show_about = True
        logging.info(locals())
        self.response.out.write(template.render(path,locals()))

