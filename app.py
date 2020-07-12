from flask import Flask
from flask import jsonify
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import settings
from util import Util

app = Flask(__name__)

socketio = SocketIO(app)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS

db = SQLAlchemy(app)
api = Api(app)
api.prefix = '/api'

migrate = Migrate(app, db)

from endpoints.HealthCheckEndpoint import HealthCheckEndpoint

api.add_resource(HealthCheckEndpoint, '/health_check')

from managers.SocketManager import *

if __name__ == '__main__':
    Util.print_banner()
    socketio.run(app, debug=True)
