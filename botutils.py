import os

class Config(object):
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT') or 5701
    base_url = os.environ.get('BASE_URL') or "http://127.0.0.1:5700/"