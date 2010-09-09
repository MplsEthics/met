"""
Classes and other utilities related to dynamic question content.
"""

from met.model import Scenario


class InvalidAnswerError(Exception):

    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class LearnerScenario(object):
    """Objects of this class handle interactions between scenarios and learner
    sessions."""

    prompt = "FIXME, maybe use getattr?"

    def __init__(self, scenario_id, session):
        """Construct the hybrid object."""
        self.scenario_id = scenario_id
        self.session = session
        self.scenario = Scenario.get_by_key_name(scenario_id)

    def is_completed(self):
        """Returns True if this learner has completed this scenario."""
        session = self.session
        scenario_id = self.scenario_id
        try:
            return session['completed'].get(scenario_id,False)
        except:
            return False

    def learner_answers(self):
        return self.session.get(self.scenario_id, [])

    def last_answer(self):
        """Returns the learner's last answer to this scenario, or None if no
        last answer exists."""
        try:
            return self.learner_answers()[-1]
        except:
            return None

    def answers(self):
        return self.answer_set

    def scenario_answers(self):
        """Returns the source answers for this scenario."""
        #FIXME
        pass

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
                setattr(a,"class","answer")
                setattr(a,"disabled",False)
            # answers chosen
            else:
                setattr(a,"disabled",True)
                # correct answer

    def mark_single_answer(self,answer,learner_answers):

        if answer.id not in learner_answers:
            setattr(answer,"class","answer")
            setattr(answer,"disabled",False)
        else:
            setattr(answer,"disabled",True)
            if answer.correct:
                setattr(answer,"class","answer correct")
            else:
                setattr(answer,"class","answer incorrect")

    def is_valid_answer(self,answer_id):
        """Returns True if answer_id is valid for this scenario."""
        valid_answer_ids = scenario.answer_dict.keys()
        return answer_id in valid_answer_ids

    def record_answer(self,answer_id):
        """Record this answer and responds accordingly."""

        if not self.is_valid_answer(answer_id):
            raise InvalidAnswerError

        # record the answer ID
        if answer_id not in self.session[scenario_id]:
            learner_answers = self.session[scenario_id]
            learner_answers.append(answer_id)
            self.session[scenario_id] = learner_answers

        # update session['completed'] if the answer is correct
        answer_obj = scenario.answer_dict[answer_id]
        if answer_obj.correct:
            completed = self.session["completed"]
            completed[scenario_id] = datetime.now().isoformat()
            self.session["completed"] = completed
