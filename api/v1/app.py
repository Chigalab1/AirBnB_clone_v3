#!/usr/bin/python3
"""Endpoint (route)
    Return the status of your API
"""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views

# creating a Flask app
app = Flask(__name__)

# registering blueprint
app.register_blueprint(app_views, url_prefix="/api/v1")


# handling 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Not found"}, 404


# handling 400 errors
@app.errorhandler(400)
def page_not_found(e):
    message = e.description
    return message, 400


# closing the app context
@app.teardown_appcontext
def close(ctx):
    storage.close()


# setting host and port
if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000

# running the Flask app
if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
