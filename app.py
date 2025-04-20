from flask import Flask, request, jsonify, send_from_directory

import requests
app = Flask(__name__, static_folder="frontend")



API_KEY="qavtgcGD.YiLCZfeRG1Rddzu360mYqB1WHNnbrpfK"
URL="https://payload.vextapp.com/hook/RZ7RL86F2P/catch/hello"
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")
@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("query")
    
    headers = {
        "Content-Type": "application/json",
        "Apikey": f"Api-Key {API_KEY}"
    }
    
    data = {
        "payload": user_input
    }

    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)