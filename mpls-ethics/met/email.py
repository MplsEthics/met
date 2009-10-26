#!/usr/bin/env python2.4

from google.appengine.api import mail

class ConfirmUserSignup(webapp.RequestHandler):
    def post(self):
        user_address = self.request.get("email_address")

        if not mail.is_email_valid(user_address):
            # prompt user to enter a valid address

        else:
            confirmation_url = createNewUserConfirmation(self.request)
            sender_address = "Example.com Support <support@example.com>"
            subject = "Confirm your registration"
            body = """
Thank you for creating an account!  Please confirm your email address
by clicking on the link below:
%s
""" % confirmation_url

            mail.send_mail(sender_address, user_address, subject, body)

