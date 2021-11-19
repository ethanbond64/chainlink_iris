import os
from datetime import timedelta

DEBUG=True
SECRET_KEY='temp'
REMEMBER_COOKIE_DURATION=timedelta(days=90)
SERVER_NAME=os.getenv('SERVER_NAME')
SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Celery.
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5