from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/random-number", methods=["GET"])
def random_number():
    wait_time = random.uniform(0, 1) 
    time.sleep(wait_time)
    number = random.randint(1, 100)
    return jsonify({"number": number, "waited_seconds": round(wait_time, 2)})

@app.route("/square/<int:value>", methods=["GET"])
def square_value(value):
    wait_time = random.uniform(0, 1) 
    result = value * value
    return jsonify({"input": value, "square": result, "waited_seconds": round(wait_time, 2)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
