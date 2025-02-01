from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set up Gemini API key
os.environ["API_KEY"] = "AIzaSyBoakTUf4je7Et5z8iGGwmza4nniyekXBY"
genai.configure(api_key=os.environ["API_KEY"])

@app.route('/ask', methods=['POST'])
def ask_gemini():
    try:
        data = request.get_json()
        query = data.get("question")
        
        if not query:
            return jsonify({"error": "No question provided"}), 400
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        
        return jsonify({"question": query, "response": response.text if response else "No response received."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
