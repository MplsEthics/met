import os
import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from met import content
from met import session

import base

class Scenario(base.BaseView):

    def get(self,scenario_id,view):
        if view != 'scenario':
            a = "%s/%s.djt" % (scenario_id, view)
            path = self.viewpath(append=a)
            djt = {
                'next': self.next(),
                'previous': self.previous(),
                's': content.get_scenario(scenario_id),
            }
            self.response.out.write(template.render(path,djt))
        else:
            self.get_scenario(scenario_id)

    def get_scenario(self,scenario_id):
        scenario = content.get_scenario(scenario_id)
        session = self.getSession()
        path = self.viewpath(append='scenario.djt')
        last_answer = self.most_recent_answer(scenario_id)
        djt = {
            'previous': self.previous(),
            'next': self.next(),
            's': scenario,
            'session': session,
            'is_correct': scenario.is_correct(last_answer),
        }
        self.response.out.write(template.render(path,djt))

    def most_recent_answer(self,scenario_id):
        session = self.getSession()
        try:
            return session[scenario_id][-1]
        except:
            return None

    def post(self,scenario_id,view):
        """Process the answer submission, then redirect to the question
        view."""
        scenario = content.get_scenario(scenario_id)
        session = self.getSession()
        answer = self.request.params['answer']
        prev_answers = session.get(scenario_id,[])
        if answer not in prev_answers:
            session[scenario_id] = prev_answers + [answer]
        self.redirect("/%s/scenario" % scenario_id)

Scenario.__bases__ += (session.SessionMixin,)
