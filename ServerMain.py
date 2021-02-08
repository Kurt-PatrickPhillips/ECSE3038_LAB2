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
tankNum = 0
tank_DB = []


@app.route("/")
def home():
    return "ECSE LAB2"


@app.route("/profile", methods=["GET", "POST", "PATCH"])
def profile():
    if request.method == "PATCH":
        UserProfile["data"]["last_updated"] = (dte.strftime("%c"))

         tempDict = request.json
          attributes = tempDict.keys()

           for attribute in attributes:
                UserProfile["data"][attribute] = tempDict[attribute]

            return jsonify(UserProfile)
    if request.method == "POST":
        UserProfile["data"]["last_updated"] = (dte.strftime("%c"))
        UserProfile["data"]["username"] = (request.json["username"])
        UserProfile["data"]["role"] = (request.json["role"])
        UserProfile["data"]["color"] = (request.json["color"])

        return jsonify(UserProfile)

    else:
        return jsonify(UserProfile)


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        global Num
        Num += 1
        posts = {}
        posts["id"] = Num
        posts["location"] = (request.json["location"])
        posts["lat"] = (request.json["lat"])
        posts["long"] = (request.json["long"])
        posts["percentage_full"] = (request.json["percentage_full"])

        tank_DB.append(posts)
        return jsonify(tank_DB)

    else:
        return jsonify(tank_DB)


@app.route("/data/<int:tankID>", methods=["PATCH", "DELETE"])
def update(tankID):
    if request.method == "PATCH":
        for index in tank_DB:
            if index["id"] == tankID:
                tempDict = request.json
                attributes = tempDict.keys()

                for attribute in attributes:
                    index[attribute] = tempDict[attribute]

        return jsonify(tank_DB)

    elif request.method == "DELETE":
        for index in tank_DB:
            if index["id"] == tankID:
                tank_DB.remove(index)

        return jsonify(tank_DB)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )
