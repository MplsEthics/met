from met.model import Scenario
from pprint import pprint

pprint([x for x in  Scenario.all()])
s = Scenario.all()[0]
pprint(s.__dict__)
pprint(dir(s))
pprint(s.fields())

# try get_by_key_name
s = Scenario.get_by_key_name('coi1')
pprint(s.__dict__)

# how does it fail?
s = Scenario.get_by_key_name('coi99')
pprint(s.__dict__)
