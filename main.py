from flask import Flask, request
import tensorflow as tf
import os
import json


app = Flask(__name__)

wait_est_model = tf.keras.models.load_model(os.getcwd()+"/saved_model/")

@app.route("/")
def HelloWorld():
    return "Hello There"

@app.route("/predict", methods=["POST"])
def predict():
    request_json = request.json
    input = request_json.get('data')
    prediction = wait_est_model.predict(input)

    lists = prediction.tolist()
    response = []
    if (len(lists) > 1):
        response = lists
    else:
        response = lists[0]

    response_json = {
        "result" : response
    }

    return json.dumps(response_json)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)