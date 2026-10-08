from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample data served by API
data = [
    {"title": "Pomodoro Timer", "description": "Boost productivity with timed focus sessions."},
    {"title": "Password Manager", "description": "Securely store and retrieve your passwords."},
    {"title": "Weather Notifier", "description": "Get daily weather updates via email."}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)