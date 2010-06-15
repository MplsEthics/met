"""
Classes and other utilities related to dynamic question content.
"""

import copy
from met.model import Scenario

def get_scenario(scenario_id):
    """Finds the scenario corresponding to the indicated ID.  We return a
    copy, because GAE persists the 'testbank' global, and we don't want any
    scary action-at-a-distance.  That might take hours to debug!"""
    return Scenario.gql("WHERE id = :1",scenario_id).get()


class InvalidAnswerError(Exception):

    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class LearnerScenario(object):
    """Objects of this class handle interactions between scenarios and learner
    sessions."""

    def __init__(self,scenario_id,session):
        """Construct the hybrid object."""
        self.scenario_id = scenario_id
        self.session = session
        self.scenario = Scenario.gql("WHERE id = :1", scenario_id).get()

    def is_completed(self):
        """Returns True if this learner has completed this scenario."""
        try:
            return self.session['completed'].get(self.scenario_id,False)
        except:
            return False

    def learner_answers(self):
        return self.session.get(self.scenario_id,[])

    def last_answer(self):
        """Returns the learner's last answer to this scenario, or None if no
        last answer exists."""
        try:
            return self.learner_answers()[-1]
        except:
            return None

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


#    def answer_dict(self):
#        """Returns a dictionary of answers?"""
#
#    # if the scenario has been completed, disable all user inputs, and set the
#    # user response to the correct value
#    if scenario.completed:
#        for a in scenario.answers:
#            setattr(a,"disabled",True)
#            if a.correct:
#                setattr(a,"class","answer correct")
#                setattr(scenario,"response",a.response)
#            else:
#                setattr(a,"class","answer incorrect")
#
#    # since the scenario has *not* been completed, make sure the response is
#    # for the **most recent** answer
#    else:
#        scenario.answer_dict[last_answer].checked = True
#        scenario.response = scenario.answer_dict[last_answer].response
#
#    return scenario
#

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

