#!/usr/bin/env python2.4

from google.appengine.api import mail

def send_completion(learner_name,learner_board):
    """Sends the completion email to someone who tracks these things."""
    sender = 'Ethics Training Completion <completion@mpls-ethics.appspotmail.com>'
    recipient = 'Ethics Education <ethicseducation@ci.minneapolis.mn.us>'
    jt = 'John Trammell <johntrammell@gmail.com>'
    subject = "Ethics training completion"
    body = """
The following user has completed their online ethics training:
    name:  %s
    board: %s
""" % (learner_name, learner_board)
    mail.send_mail(sender, recipient, subject, body, bcc=jt),

