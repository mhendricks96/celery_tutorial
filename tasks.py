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

@app.task
def nothing(x,y):
  pass

@app.task
def do_stuff():
  from selenium import webdriver
  import time
  driver = webdriver.Chrome()
  time.sleep(30)
  driver.get('https://frontrowviews.com/Home/Event/ProviderDetails/5a83c3f209310b1d68d45c46')