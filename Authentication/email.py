from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from decouple import config
from django.utils.html import strip_tags

def send_welcome_email(name,password,receiver):
    email_template = 'email/email.html'
    context = {'name': name, 'password': password}

    # Render the email template with the context data
    html_message = render_to_string(email_template, context)
    plain_message = strip_tags(html_message)

    # Set the email subject, sender, recipient(s), and message content
    subject = 'Eazz Employee Account Password'
    from_email = config('EMAIL_HOST_USER')
    recipient_list = [receiver]
    message = plain_message
    html_message = html_message

    # Send the email using the send_mail function
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    # Creating message subject and sender
   