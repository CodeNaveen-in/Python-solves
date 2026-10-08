from flask import Flask, render_template

app = Flask(__name__)

# Sample project list
projects = [
    "Pomodoro Timer",
    "Password Manager",
    "Flashcard App",
    "Quiz Game",
    "Weather Notifier",
    "ISS Tracker",
    "Salary Analyzer",
    "Blog API",
    "Morse Code Converter",
    "Nobel Prize Visualizer"
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)