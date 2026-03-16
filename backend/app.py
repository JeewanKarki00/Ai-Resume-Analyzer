from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def home():

    return "AI Resume Analyzer Backend Running"

@app.route("/analyze", methods=["POST"])

def analyze_resume():

    if 'file' not in request.files:

        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    return jsonify({

        "message": "Resume received",

        "filename": file.filename

    })

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
