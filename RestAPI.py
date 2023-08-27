from flask import Flask,jsonify

players = [{"Name": "Dhoni","batting_style": "Right-hand-bat","Team":"India"},
           {"Name": "Williamson","batting_style": "Right-hand-bat","Team":"New Zealand"},
           {"Name": "Ben Stokes","batting_style": "Left-hand-bat","Team":"England"}]


app = Flask(__name__)
@app.route('/')
def index():
    return "Hello"

@app.route("/players",methods=['GET'])
def get():
    return jsonify({"players": players})

@app.route("/players/<int:Name>",methods=['GET'])
def get_players(Name):
    return jsonify({"players" : players[Name]})

@app.route("/players",methods=['POST'])
def create():
    player = {"Name": "Babar Azam","batting_style": "Right-hand-bat","Team":"Pakistan"}
    players.append(player)
    return jsonify({'Created': players})

@app.route("/players/<int:Name>",methods=['PUT'])
def update(Name):
    players[Name]["Team"] = "Australia"
    return jsonify ({"player": players[Name]})


@app.route("/players/<int:Name>",methods=['DELETE'])
def delete(Name):
    players.remove(players[Name])
    return jsonify({"result" : True})

if __name__ == "__main__":
    app.run(debug=True)