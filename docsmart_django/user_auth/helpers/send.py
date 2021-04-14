from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class SendMail:

    @staticmethod
    def send_invite(current_user, invited_user, url):
        subject = 'Invitation: ' + current_user.first_name + ' ' + current_user.last_name + \
                  ' sent you an invite to join them on DocSmart'
        html_message = render_to_string('invite.html', {'url': url, 'name': invited_user.email})
        plain_message = strip_tags(html_message)
        from_email = 'From <postmaster@sandbox1be520cdb9fe45a0b76cef31d274d7a6.mailgun.org>'
        to = "gbemilanre@gmail.com"
        # to = invited_user.email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    @staticmethod
    def send_confirmation_mail(user, url):
        subject = 'Welcome To DocSmart'
        html_message = render_to_string('welcome.html', {'url': url, 'name': 'David'})
        plain_message = strip_tags(html_message)
        from_email = 'From <postmaster@sandbox1be520cdb9fe45a0b76cef31d274d7a6.mailgun.org>'
        to = "gbemilanre@gmail.com"

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
