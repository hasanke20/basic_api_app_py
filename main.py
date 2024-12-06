from flask import flask, jsonify
from datetime import datetime

app = flask(__name__)

@app.route('/getquote', methods=['get'])
def get_quote():
    response = {
        "result": true,
        "timestamp": datetime.now().isoformat(),
        "data": {
            "quote": "melali anlamayan nesle asina degiliz.",
            "author": "ahmet hasim"
        }
    }
    return jsonify(response)

@app.route('/ping', methods=['get'])
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
