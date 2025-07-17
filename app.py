from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Service is up!"

@app.route('/score-lead', methods=['GET', 'POST'])
def score_lead():
    if request.method == 'GET':
        return "score-lead GET is working!"
    if request.method == 'POST':
        try:
            data = request.json
            print("Received:", data)
            # Return a fixed test score for now
            return jsonify({"score": 85})
        except Exception as e:
            print("Error:", e)
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
