"""
Classes and other utilities related to dynamic question content.
"""

from datetime import datetime
from met.model import Answer, Scenario
from met.exceptions import InvalidAnswerException



class LearnerScenario(object):
    """Handle interactions between scenarios and learner sessions."""

    def __init__(self, scenario_id, session):
        """Construct the hybrid object."""
        self.scenario_id = scenario_id
        self.scenario = Scenario.get_by_key_name(scenario_id)
        self.session = session

    def __getattr__(self, name):
        return getattr(self.scenario, name)

    def is_completed(self):
        """Returns True if this learner has completed this scenario."""
        session = self.session
        scenario_id = self.scenario_id
        return session['completed'].get(scenario_id, False)

    def learner_answers(self):
        return self.session.get(self.scenario_id, [])

    def last_answer(self):
        """Returns the learner's last answer to this scenario, or None if no
        last answer exists."""
        try:
            return self.learner_answers()[-1]
        except:
            return None

    def annotated_answers(self):

        def annotate(answer):
            # FIXME: need to incorporate logic from below...
            a = answer.as_dict()
            return a

        return [annotate(answer) for answer in self.answer_set]

    def marked_answers(self):

        if self.is_completed():
            pass
        else:
            answers = []

            for a in self.scenario_answers():
                d = dict(a.__dict__)

                if a.id not in self.learner_answers():
                    pass

                answers.append(d)

            # answers not yet chosen
            if a.id not in learner_answers:
                setattr(a, "class", "answer")
                setattr(a, "disabled", False)
            # answers chosen
            else:
                setattr(a, "disabled", True)
                # correct answer

    def mark_single_answer(self, answer, learner_answers):

        if answer.id not in learner_answers:
            setattr(answer, "class", "answer")
            setattr(answer, "disabled", False)
        else:
            setattr(answer, "disabled", True)
            if answer.correct:
                setattr(answer, "class", "answer correct")
            else:
                setattr(answer, "class", "answer incorrect")

    def record_answer(self, answer_id):
        """Record this answer and responds accordingly."""

        answer = Answer.get_by_key_name(answer_id)

        # if the lookup failed then this is not a valid answer
        if not answer:
            raise InvalidAnswerException

        # record the answer ID
        session = self.session
        scenario_id = self.scenario_id
        if answer_id not in session[scenario_id]:
            session[scenario_id] += [answer_id]

        # update session['completed'] if the answer is correct
        if answer.is_correct:
            completed = session["completed"]
            completed[scenario_id] = datetime.now().isoformat()
            session["completed"] = completed
