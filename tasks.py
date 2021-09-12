from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

import os

# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_tutorial.settings')


@app.task
def add(x, y):
    return x + y

@app.task
def multiply(x, y):
    return x * y

@app.task
def divide(x, y):
    return x / y

# @app.task
# def subtract(x, y):
#     return (x - y)

from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine, Context

def render_template(template, context):
    engine = Engine.get_default()

    tmpl = engine.get_template(template)

    return tmpl.render(Context(context))

@app.task
def send_mail_task(recipients, subject, template, context):
    send_mail(
        subject=subject,
        message=render_template(f'{template}.txt', context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        fail_silently=False,
        html_message=render_template(f'{template}.html', context)
    )