from celery import Celery
from flask import Flask
from server.utils.extensions import db, socketio
from server.blueprints.main import main, streaming, generator

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('utils/settings.py', silent=True)
    db.init_app(app)
    # uncomment this for first run
    # db.drop_all(app=app)
    db.create_all(app=app)
    app.register_blueprint(main)
    app.register_blueprint(streaming)
    app.register_blueprint(generator)
    socketio.init_app(app)

    return app

CELERY_TASK_LIST = [
    'server.blueprints.main.tasks'
]
# From Nick Janetakis
def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


