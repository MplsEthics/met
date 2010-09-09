"""
This module implements a custom Session class for the Minneapolis Ethics
Training site.  It extends the Appengine Utilities ("GAEUtilities") sessions
class (see http://code.google.com/p/gaeutilities/).
"""

from pprint import pformat
from datetime import datetime
from appengine_utilities.sessions import Session as GAESession
from met.order import scenario_order
from met.model import Answer, Scenario
from met.exceptions import InvalidAnswerException


class Session(GAESession):
    """Subclass the appengine_utilities session object to simplify
    extension."""

    def __init__(self, *args, **kwargs):
        """Initialize session attributes for the ethics training."""

        # call parent init
        super(Session, self).__init__(*args, **kwargs)

        # initialize scenario answer array
        for s in scenario_order:
            if not s in self:
                self[s] = []

        # initialize scenario completion dictionary
        if not 'completed' in self:
            items = [(s, False) for s in scenario_order]
            self['completed'] = dict(items)


class LearnerState(object):
    """Handles all interactions with the learner's state."""

    def __init__(self):
        """Construct the state object."""
        pass

    def session(self):
        """Cache and return an initialized session object."""
        if getattr(self, '_session', None) is None:
            self._session = Session()
        return self._session

    def session_fmt(self):
        session = self.session()
        return pformat(dict(session.items()))

    def is_completed(self, scenario_id):
        """Returns True if this learner has completed this scenario."""
        completed = self.session()['completed']
        return completed[scenario_id]

    def completed_prerequisites(self, scenario_id):
        """Returns True if all the scenarios before 'scenario_id' have been
        completed; returns False otherwise."""

        assert scenario_id in scenario_order, 'unknown scenario'

        # search through all the scenarios in order, making sure the learner
        # has completed each
        for s in scenario_order:
            if s == scenario_id:
                return True
            elif not self.is_completed(s):
                return False

    def first_incomplete_scenario(self):
        completed = self.session()['completed']
        for s in scenario_order:
            if not completed[s]:
                return s
        return None

    def learner_answers(self, scenario_id):
        session = self.session()
        return session[scenario_id]

    def last_answer_id(self, scenario_id):
        """Returns the most recent answer the learner gave to the indicated
        scenario, or None if the student has no answers yet in that
        scenario."""
        try:
            return self.learner_answers(scenario_id)[-1]
        except:
            return None

    def annotate_scenario(self, scenario_id):
        scenario = Scenario.get_by_key_name(scenario_id).as_dict()
        scenario['answers'] = self.annotated_answers(scenario_id)
        scenario['is_completed'] = self.is_completed(scenario_id)
        return scenario

    def annotated_answers(self, scenario_id):
        """Returns a list of dicts reflecting the correct learner state for
        scenario_id."""

        scenario = Scenario.get_by_key_name(scenario_id)
        is_completed = self.is_completed(scenario_id)
        learner_answers = self.learner_answers(scenario_id)

        def annotate(answer):
            """Convert the Answer object into a marked-up dict"""
            a = answer.as_dict()
            # if this scenario has been completed, we want the correct answer
            # to be highlighted
            if is_completed or a['name'] in learner_answers:
                a['disabled'] = True
                if answer.is_correct:
                    a['class'] = "answer correct"
                else:
                    a['class'] = "answer incorrect"
            else:
                a['disabled'] = False
                a['class'] = "answer"
            return a

        return [annotate(answer) for answer in scenario.answer_set]

    def record_answer(self, scenario_id, answer_id):
        """Record this answer in the session; do any necessary updates."""

        answer = Answer.get_by_key_name(answer_id or '--none--')

        # if the lookup failed then this is not a valid answer
        # FIXME: need to check answer/scenario matching
        if not answer:
            raise InvalidAnswerException('bad answer ID')

        # record the answer ID
        session = self.session()
        if answer_id not in session[scenario_id]:
            session[scenario_id] += [answer_id]

        # update session['completed'] if the answer is correct
        if answer.is_correct:
            completed = session["completed"]
            completed[scenario_id] = datetime.now().isoformat()
            session["completed"] = completed
