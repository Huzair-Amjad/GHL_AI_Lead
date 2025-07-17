from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/score-lead', methods=['POST'])
def score_lead():
    data = request.json
    print("Received:", data)
    return jsonify({"score": 85})

@app.route('/', methods=['GET'])
def home():
    return "Service is up!"
