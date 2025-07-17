from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- Allow cross-origin requests

@app.route('/', methods=['GET'])
def home():
    return "Service is up!"

@app.route('/score-lead', methods=['GET', 'POST'])
def score_lead():
    if request.method == 'GET':
        return "score-lead GET is working!"
    if request.method == 'POST':
        data = request.json
        print("Received:", data)
        return jsonify({"score": 85})

if __name__ == "__main__":
    app.run()
