from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/riddle", methods=["POST"])
def solve():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "no question"}), 400
    question = data["question"]
    prompt = (
        "You are solving riddles for the Roblox game 'Steal a Brainrot' (SAB). "
        "The owner is named Sammy (SPYDERSAMMY on Roblox). "
        "Answer ONLY with the answer word(s), no explanation, no punctuation, uppercase only. "
        "Example: if asked 'what is my favorite color' answer: BLUE\n\n"
        f"Question: {question}"
    )
    response = model.generate_content(prompt)
    answer = response.text.strip().upper().replace(" ", "")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
