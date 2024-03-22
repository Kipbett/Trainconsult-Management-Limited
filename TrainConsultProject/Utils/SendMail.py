from django.core.mail import send_mail


def send_custom_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)