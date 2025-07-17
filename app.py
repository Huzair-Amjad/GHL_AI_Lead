from flask import Flask, request, jsonify
from openai import OpenAI
app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route('/score-lead', methods=['POST'])
def score_lead():
    print("Received a POST to /score-lead")
    data = request.json
    prompt = f"""Score the following sales lead from 0 (cold) to 100 (hot) based on their info for a marketing agency. Just return the score number.\n\nLead: {data}"""
    stream = client.chat.completions.create(
        model="text-davinci-003",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5,
        temperature=0
    )
    for chunk in stream:
      if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end = "")

if __name__ == '__main__':
    app.run(debug=True)
