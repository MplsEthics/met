# Copyright 2012 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics
# is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

"""
This module implements a custom Session class for the Minneapolis Ethics
Training site.  It extends the Appengine Utilities ("GAEUtilities") sessions
class (see http://code.google.com/p/gaeutilities/).
"""

from pprint import pformat
from datetime import datetime
from met.boards import boards
from met.order import scenario_order
from met.model import Answer, Completion, Scenario
from met.exceptions import InvalidAnswerException, InvalidLearnerException


class LearnerState(object):
    """
    Handles all interactions with the learner's state, which is presumably
    stored in some sort of session object.
    """

    def __init__(self, session):
        """Construct the state object."""
        self.session = session

    def as_string(self):
        """Returns the learner state as a string."""
        return pformat(dict(self.session))

    def update_timestamp(self):
        """Only save the last few timestamps!"""
        timestamps = self.session.get('timestamp', [])
        timestamps += [datetime.now().isoformat()]
        self.session['timestamp'] = timestamps[0:3]

    def is_completed(self, scenario_id):
        """Returns True if this learner has completed this scenario."""
        completed = self.session.get('completed', {})
        return completed.get(scenario_id, False)

    def completed_all(self):
        """Returns True if the user has completed all scenarios."""
        completed = self.session()['completed']
        for s in scenario_order:
            if s not in completed:
                return False
        return True

    def completed_prerequisites(self, scenario_id):
        """Returns True if all the scenarios before 'scenario_id' have been
        completed; returns False otherwise."""

        assert scenario_id in scenario_order, 'unknown scenario'

        # make sure the learner has completed all scenarios
        # prior to scenario_id
        for s in scenario_order:
            if s == scenario_id:
                return True
            elif not self.is_completed(s):
                return False

    def first_incomplete_scenario(self):
        completed = self.session()['completed']
        for s in scenario_order:
            if not completed[s]:
                return s
        return None

    def learner_answers(self, scenario_id):
        return self.session.get(scenario_id, [])

    def last_answer_id(self, scenario_id):
        """Returns the most recent answer the learner gave to the indicated
        scenario, or None if the student has no answers yet in that
        scenario."""
        try:
            return self.learner_answers(scenario_id)[-1]
        except:
            return None

    def annotate_scenario(self, scenario_id):
        scenario = Scenario.get_by_key_name(scenario_id).as_dict()
        scenario['answers'] = self.annotated_answers(scenario_id)
        scenario['is_completed'] = self.is_completed(scenario_id)
        return scenario

    def annotated_answers(self, scenario_id):
        """
        Returns a list of dicts reflecting the correct learner state for
        scenario_id.
        """

        scenario = Scenario.get_by_key_name(scenario_id)
        is_completed = self.is_completed(scenario_id)
        learner_answers = self.learner_answers(scenario_id)

        def annotate(answer):
            """Convert the Answer object into a marked-up dict"""
            a = answer.as_dict()
            # if this scenario has been completed, we want the correct answer
            # to be highlighted
            if is_completed or a['name'] in learner_answers:
                a['disabled'] = True
                if answer.is_correct:
                    a['class'] = "answer correct"
                else:
                    a['class'] = "answer incorrect"
            else:
                a['disabled'] = False
                a['class'] = "answer"
            return a

        return [annotate(answer) for answer in scenario.answer_set]

    def record_answer(self, scenario_id, answer_id):
        """Record this answer in the session; do any necessary updates."""

        # make sure the session has the fields I need
        self.session.setdefault(scenario_id, {})
        self.session.setdefault('completed', {})

        # get the correct answer
        answer = Answer.get_by_key_name(answer_id or '--none--')

        # if the lookup failed then this is not a valid answer
        if not answer:
            raise InvalidAnswerException('bad answer ID')

        # verify that this answer is for this scenario
        if not answer.scenario.key().name() == scenario_id:
            raise InvalidAnswerException('answer and scenario do not match')

        # record the answer ID
        if answer_id not in self.session[scenario_id]:
            self.session[scenario_id] += [answer_id]

        # update session['completed'] if the answer is correct
        if answer.is_correct:
            self.session['completed'][scenario_id] = datetime.now().isoformat()

    def learner_error(self, error=False):
        session = self.session()
        session['learner_error'] = True if error else False
        return session['learner_error']

    def learner_name(self):
        return self.session().get('learner_name', None)

    def learner_board(self):
        return self.session().get('learner_board', None)

    def learner_date(self):
        return self.session().get('learner_date', None)

    def persist_learner(self, name, board_id, date):
        """Check the learner info; if it's good, persist it in the session and
        GAE storage."""
        session = self.session()

        # perform sanity checks on the name and the board
        try:
            if len(name) == 0:
                raise
            board = boards[int(board_id)]
            if len(board) == 0:
                raise
        except:
            self.learner_error(True)
            msg = "name='%s' board_id='%s'" % (name, board_id)
            raise InvalidLearnerException(msg)

        # persist the learner name and board in the session (to be used by the
        # certificate template)
        session['learner_name'] = name
        session['learner_board'] = board

        # if the date is not empty, convert to datetime and persist
        if date:
            session['learner_date'] = datetime.strptime(date, "%m/%d/%Y")
        elif 'learner_date' in session:
            del session['learner_date']

        # persist the learner name, board, and a timestamp in GAE storage
        # (the timestamp should be created automatically)
        comp = Completion()
        comp.name = name
        comp.board = board
        comp.put()
