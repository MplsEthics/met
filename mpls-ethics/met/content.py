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
            setattr(a,"disabled",True)
            # correct answer
            if a.correct:
                setattr(a,"class","answer correct")
            # incorrect answer
            else:
                setattr(a,"class","answer incorrect")

    # if the session says to, mark this scenario as completed
    if session['completed'].get(scenario_id,False):
        scenario.completed = True
    else:
        scenario.completed = False

    # if the scenario has been completed, disable all user inputs, and set the
    # user response to the correct value
    if scenario.completed:
        for a in scenario.answers:
            setattr(a,"disabled",True)
            if a.correct:
                setattr(a,"class","answer correct")
                setattr(scenario,"response",a.response)
            else:
                setattr(a,"class","answer incorrect")

    # since the scenario has *not* been completed, make sure the response is
    # for the **most recent** answer
    else:
        scenario.answer_dict[last_answer].checked = True
        scenario.response = scenario.answer_dict[last_answer].response

    return scenario

if __name__ == '__main__':
    print 'file: %s' % __file__
    pprint(testbank)

