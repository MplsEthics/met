"""
Classes and other utilities related to dynamic question content.
"""

import copy
from met.model import Scenario

def get_scenario(scenario_id):
    """Finds the scenario corresponding to the indicated ID.  We return a
    copy, because GAE persists the 'testbank' global, and we don't want any
    scary action-at-a-distance.  That might take hours to debug!"""
    scenario = testbank.get(scenario_id,None)
    return copy.deepcopy(scenario)

def merge_scenario(scenario_id,session):
    """Retrieve the raw scenario data, then append information to it based on
    the learner status in the session.  This function does quite a bit; it
    should definitely be refactored."""

    scenario = get_scenario(scenario_id)

    # get the learner's answers to this scenario
    learner_answers = session.get(scenario_id,[])

    # if there are no learner answers yet, we don't need to do anything
    if not learner_answers:
        return scenario

    # find the user's most recent answer to this scenario, if any
    try: last_answer = learner_answers[-1]
    except: last_answer = None

    # set attributes on the answer objects
    for a in scenario.answers:
        # answers not yet chosen
        if a.id not in learner_answers:
            setattr(a,"class","answer")
            setattr(a,"disabled",False)
        # answers chosen
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

