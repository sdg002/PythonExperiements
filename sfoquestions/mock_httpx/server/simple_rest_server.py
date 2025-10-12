import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def weather():
    records= [{"city": "LDN", "temperature": random.randint(20, 30)},
              {"city": "PAR", "temperature": random.randint(15, 25)},
              {"city": "NYC", "temperature": random.randint(10, 20)}]
    return jsonify(records)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
