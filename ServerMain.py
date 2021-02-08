from flask import flask, request, jsonify
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
dte = datetime.datetime.now()
UserProfile = {
    "sucess": True,
    "data": {
        "last_updated": "",
        "username": "Hannibal",
        "role": "Engineer",
        "color": "yellow"
    }
}
