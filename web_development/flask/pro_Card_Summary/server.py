from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/naveen')
def nv():
    return render_template("naveen.html")

if (__name__ == "__main__"):
    app.run(debug=True)