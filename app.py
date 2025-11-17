import os
import json
from flask import Flask, render_template, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

def load_json(filename):
    path = os.path.join(BASE_DIR, "data", f"{filename}.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_json("index")
    return render_template("index.html", data=data)

@app.route('/subject')
def subject():
    data = load_json("subject")
    return render_template("subject.html", data=data)

@app.route('/rationale')
def rationale():
    data = load_json("rationale")
    return render_template("rationale.html", data=data)

@app.route('/features')
def features():
    data = load_json("features")
    return render_template("features.html", data=data)

@app.route('/environment')
def environment():
    data = load_json("environment")
    return render_template("environment.html", data=data)

@app.route('/team')
def team():
    data = load_json("team")
    return render_template("team.html", data=data)

# API endpoints
@app.route('/api/subject')
def api_subject():
    return jsonify(load_json("subject"))

@app.route('/api/rationale')
def api_rationale():
    return jsonify(load_json("rationale"))

@app.route('/api/features')
def api_features():
    return jsonify(load_json("features"))

@app.route('/api/environment')
def api_environment():
    return jsonify(load_json("environment"))

@app.route('/api/team')
def api_team():
    return jsonify(load_json("team"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)