"""
This module implements a custom Session class for the Minneapolis Ethics
Training site.  It uses the Appengine Utilities ("GAEUtilities") sessions
class as its basis (see http://code.google.com/p/gaeutilities/).
"""

from appengine_utilities.sessions import Session as GAESession
from met.order import scenario_order

class Session(GAESession):
    """Subclass the appengine_utilities session object to simplify
    extension."""

    def __init__(self, *args, **kwargs):
        """Initialize session attributes for the ethics training."""

        # call parent init
        super(Session,self).__init__(*args, **kwargs)

        # init scenario answer array
        for so in scenario_order:
            self.setdefault(so,[])

        # init scenario completion dict
        self.setdefault('completed',dict())
