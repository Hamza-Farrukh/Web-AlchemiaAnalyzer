from flask import Flask, send_from_directory
from flaskwebgui import FlaskUI
from AlchemiaStoryTools.wsgi import application as app
from django.core.wsgi import get_wsgi_application
from django.conf import settings

import os

django_app = get_wsgi_application()
app = Flask(__name__, static_folder='static')


@app.route('/media/<path:filename>', methods=['POST', 'GET'])
def media_files(filename):
    media_root = settings.MEDIA_ROOT
    return send_from_directory(media_root, filename)


@app.route('/', methods=['POST', 'GET'])
def login():
    return django_app


if __name__ == "__main__":
    # Add the media URL route
    app.add_url_rule('/media/<path:filename>', endpoint='media_files', view_func=media_files)
    
    FlaskUI(app=app, server="django").run()
