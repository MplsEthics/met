from google.appengine.ext import webapp
import base
from datetime import datetime
from met import content
from met import session
from met.order import scenario_order
import logging
import time

class Scenario(base.BaseView, session.SessionMixin):

    def get(self,scenario_id):
        #logging.info('GET')
        session = self.getSession()
        self.assert_scenario_order(scenario_id,session)
        scenario = content.merge_scenario(scenario_id,session)
        path = self.viewpath(append='scenario.djt')
        djt = {
            'previous': self.previous(),
            'next': self.next(),
            's': scenario,
            'session': session,
            'show_prevnext': scenario.completed,
        }
        #time.sleep(3)
        self.response.out.write(webapp.template.render(path,djt))

    def post(self,scenario_id):
        """Process the answer submission, then redirect to the "response"
        view."""
        #logging.info('POST')
        session = self.getSession()
        self.assert_scenario_order(scenario_id,session)
        scenario = content.get_scenario(scenario_id)
        valid_answer_ids = scenario.answer_dict.keys()

        # update the session as needed based on the answer
        answer = self.request.params.get('answer',None)
        if answer in valid_answer_ids:
            # save the answer
            if answer not in session[scenario_id]:
                logging.info('%s => %s' % (answer,scenario_id))
                session[scenario_id] += [ answer ]
                logging.info('>>> %s' % session[scenario_id])

            # if the answer is correct, update session.completed
            answer_obj = scenario.answer_dict[answer]
            if answer_obj.correct:
                logging.info('completed %s' % scenario_id)
                completed = session["completed"]
                completed[scenario_id] = datetime.now().isoformat()
                session["completed"] = completed
                logging.info('>>> %s' % session["completed"])

        logging.info("session: %s" % session)

        #time.sleep(3)
        self.redirect("/%s/response" % scenario_id)

    def assert_scenario_order(self,scenario_id,session):
        """If the user is accessing this scenario out of order, redirect to
        the most recently completed scenario."""
        for i in range(scenario_order.index(scenario_id)):
            test_scenario = scenario_order[i]
            if test_scenario not in session['completed']:
                self.redirect("/%s/response" % test_scenario)

