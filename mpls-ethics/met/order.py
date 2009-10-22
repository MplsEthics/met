# define the scenario order
scenario_order = [
    'coi1',
    'coi2',
    'coi3',
    'coi4',
    'doi',
    'gifts',
]

# define the navigation view order
view_order = [
    'main',
    'instr1',
    'instr2',
    'over1',
    'over2',

    # conflict of interest part 1
    'coi1/intro1',
    'coi1/intro2',
    'coi1/scenario',
    'coi1/disc1',
    'coi1/disc2',

    # conflict of interest part 2
    'coi2/intro1',
    'coi2/scenario',
    'coi2/disc1',
    'coi2/disc2',
    'coi2/disc3',

    # conflict of interest part 3
    'coi3/intro1',
    'coi3/scenario',
    'coi3/disc1',
    'coi3/disc2',
    'coi3/disc3',
    'coi3/disc4',

    # conflict of interest part 4
    'coi4/intro1',
    'coi4/scenario',
    'coi4/disc1',
    'coi4/disc2',
    'coi4/disc3',

    # disclosure of information
    'doi/intro1',
    'doi/scenario',
    'doi/disc1',

    # gifts
    'gifts/intro1',
    'gifts/intro2',
    'gifts/scenario',
    'gifts/disc1',
    'gifts/disc2',

    # ethics report line & contact info
    'reportline1',
    'reportline2',
    'reportline3',
    'summary',
    'congrats',

    # collect learner name & board
    'learner',

    # display training certificate / proof of completion
    'certificate',
]

class OrderMixin(object):

    def prereqs_completed(self,scenario_id):
        """Returns True if all the scenarios before to 'scenario_id' have been
        completed, as indicated by their status in 'compdict'.  Returns False
        otherwise.  This function can be used to determine if the user is
        trying to complete the scenarios out of order."""
        compdict = self.getSession()["completed"]
        assert scenario_id in scenario_order, 'test scenario must be known'
        k = scenario_order.index(scenario_id)
        for sid in scenario_order[0:k]:
            if sid not in compdict:
                return False
        return True

    def all_scenarios_completed(self):
        """Returns True if all the scenarios are in the dict that records
        scenario completiions ('compdict').  Returns False otherwise."""
        compdict = self.getSession()["completed"]
        for sid in scenario_order:
            if sid not in compdict:
                return False
        return True

    def first_incomplete_scenario(self):
        compdict = self.getSession()["completed"]
        for sid in scenario_order:
            if sid not in compdict:
                return sid
        return None

