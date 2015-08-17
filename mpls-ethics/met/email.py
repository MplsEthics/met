# Copyright 2015 John J. Trammell.
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

from google.appengine.api import mail

def send_completion(learner_name, learner_board):
    """Sends the completion email to someone who tracks these things."""
    msg = mail.EmailMessage()

    # send the message to 'ethics education'
    msg.sender = 'Ethics Training Completion <completion@mpls-ethics.appspotmail.com>'
    msg.to = 'Ethics Education <openappointments@minneapolismn.gov>'
    msg.subject = "Ethics training completion"
    msg.body = """
The following user has completed their online ethics training:
    name:  %s
    board: %s
""" % (learner_name, learner_board)
    msg.send()

    # send a copy to me
    msg.to = 'John Trammell <john.trammell@gmail.com>'
    msg.send()
