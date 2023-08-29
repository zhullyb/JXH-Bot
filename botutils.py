import os

class Config(object):
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT') or 5701