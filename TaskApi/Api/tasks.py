from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def sendemails():
    sleep(5)
    send_mail('COnfirmation mail',
              'Successful',
              'ShubhangiShrivas@gmail.com',
              [''])
