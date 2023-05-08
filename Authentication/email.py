from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from decouple import config

def send_welcome_email(name,password,receiver):
    # Creating message subject and sender
    subject = 'Eazz Employee Account Password'
    sender = config('EMAIL_HOST_USER')
    message = f'Hello {name}, We are happy to welcome you to your first step with Eazz, your auto generated password is {password}.We hope to eazz your journey with Eazz.'
    send_mail(subject,message,sender,recipient_list=[receiver])
   