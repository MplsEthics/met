
import ConfigParser

def read_questions():
    config = ConfigParser.RawConfigParser()
    config.read('ethics.cfg')
    return config

class Question(object):
    """ """

    def __init__(self):
        pass

