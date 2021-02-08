from flask import flask, request, jsonify
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 now = datetime.now()
dte = datetime.datetime.now()

UserProfile = [
    "success": True,
    "data": {
        "last_updated": "",
        "username": "Hannibal",
        "role": "Engineer",
        "color": "yellow"
    }
]
tankNum = 0
tankdt = []


@app.route("/")
def home():
    return "ECSE LAB2"


@app.route("/profile", methods=["GET", "POST", "PATCH"])
def profile():
       if request.method == "POST":
        UserProfile["data"]["last_updated"] = (dte.strftime("%c"))
        UserProfile["data"]["username"] = (request.json["username"])
        UserProfile["data"]["role"] = (request.json["role"])
        UserProfile["data"]["color"] = (request.json["color"])

        return jsonify(UserProfile)

    else:
        return jsonify(UserProfile)

   elif request.method == "PATCH":
        UserProfile["data"]["last_updated"] = (dte.strftime("%c"))

         tempDict = request.json
          attributes = tempDict.keys()

           for attribute in attributes:
                UserProfile["data"][attribute] = tempDict[attribute]

            return jsonify(UserProfile)



@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        global Num
        Num += 1
        posts = {}
        posts["id"] = Num
        posts["location"] = (request.json["location"])
        posts["latitude"] = (request.json["latitude"])
        posts["longitude"] = (request.json["longitude"])
        posts["percentage_full"] = (request.json["percentage_full"])

        tankdt.append(posts)
        return jsonify(tankdt)

    else:
        return jsonify(tankdt)


@app.route("/data/<int:tankNum>", methods=["PATCH", "DELETE"])
def update(tankNum):
    if request.method == "PATCH":
        for index in tankdt:
            if index["id"] == tankNum:
                tempDict = request.json
                attributes = tempDict.keys()

                for attribute in attributes:
                    index[attribute] = tempDict[attribute]

        return jsonify(tankdt)

    elif request.method == "DELETE":
        for index in tankdt:
            if index["id"] == tankNum:
                tankdt.remove(index)

        return jsonify(tankdt)


if __name__ == '__ServerMain__':
    app.run(
        debug=True,
        port=3000,
    )
