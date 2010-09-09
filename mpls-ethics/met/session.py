"""
This module implements a custom Session class for the Minneapolis Ethics
Training site.  It extends the Appengine Utilities ("GAEUtilities") sessions
class (see http://code.google.com/p/gaeutilities/).
"""

from datetime import datetime
from appengine_utilities.sessions import Session as GAESession
from met.order import scenario_order
from met.model import Answer
from met.exceptions import InvalidAnswerException


class Session(GAESession):
    """Subclass the appengine_utilities session object to simplify
    extension."""

    def __init__(self, *args, **kwargs):
        """Initialize session attributes for the ethics training."""

        # call parent init
        super(Session, self).__init__(*args, **kwargs)

        # init scenario answer array
        for so in scenario_order:
            self.setdefault(so, [])

        # init scenario completion dict
        self.setdefault('completed', dict())


class LearnerState(object):
    """Handles interactions querying and updating the user state."""

    def __init__(self):
        """Construct the state object."""
        pass

    def session(self):
        """Cache and return an initialized session object."""
        if getattr(self, '_session', None) is None:
            self._session = Session()
        return self._session

    def is_completed(self, scenario_id):
        """Returns True if this learner has completed this scenario."""
        session = self.session()
        return session['completed'].get(scenario_id, False)

    def learner_answers(self, scenario_id):
        session = self.session()
        return session.get(scenario_id, [])

    def last_answer(self, scenario_id):
        """Returns the learner's last answer to the indicated scenario, or
        None if the student has no answers yet in that scenario."""
        try:
            return self.learner_answers(scenario_id)[-1]
        except:
            return None

    def annotated_answers(self, scenario_id):
        """Returns a list of dicts reflecting the correct learner state for
        scenario_id."""

        def annotate(answer):
            # FIXME: need to incorporate logic from below...
            a = answer.as_dict()
            return a

        return [annotate(answer) for answer in self.answer_set]

### FIXME: move these functions into annotate() above...
###
###     def marked_answers(self):
###
###         if self.is_completed():
###             pass
###         else:
###             answers = []
###
###             for a in self.scenario_answers():
###                 d = dict(a.__dict__)
###
###                 if a.id not in self.learner_answers():
###                     pass
###
###                 answers.append(d)
###
###             # answers not yet chosen
###             if a.id not in learner_answers:
###                 setattr(a, "class", "answer")
###                 setattr(a, "disabled", False)
###             # answers chosen
###             else:
###                 setattr(a, "disabled", True)
###                 # correct answer
###
###     def mark_single_answer(self, answer, learner_answers):
###
###         if answer.id not in learner_answers:
###             setattr(answer, "class", "answer")
###             setattr(answer, "disabled", False)
###         else:
###             setattr(answer, "disabled", True)
###             if answer.correct:
###                 setattr(answer, "class", "answer correct")
###             else:
###                 setattr(answer, "class", "answer incorrect")

    def record_answer(self, scenario_id, answer_id):
        """Record this answer in the session."""

        answer = Answer.get_by_key_name(answer_id)

        # if the lookup failed then this is not a valid answer
        if not answer:
            raise InvalidAnswerException

        # record the answer ID
        session = self.session
        if answer_id not in session[scenario_id]:
            session[scenario_id] += [answer_id]

        # update session['completed'] if the answer is correct
        if answer.is_correct:
            completed = session["completed"]
            completed[scenario_id] = datetime.now().isoformat()
            session["completed"] = completed
