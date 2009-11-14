#!/usr/bin/env python2.4

from google.appengine.api import mail

def send_completion(learner_name,learner_board):
    """Sends the completion email to someone who tracks these things."""
    msg = mail.EmailMessage()

    # send the message to 'ethics education'
    msg.sender = 'Ethics Training Completion <completion@mpls-ethics.appspotmail.com>'
    msg.to = 'Ethics Education <ethicseducation@ci.minneapolis.mn.us>'
    msg.subject = "Ethics training completion"
    msg.body = """
The following user has completed their online ethics training:
    name:  %s
    board: %s
""" % (learner_name, learner_board)
    msg.send()

    # send a copy to me
    msg.to = 'John Trammell <johntrammell@gmail.com>'
    msg.send()

