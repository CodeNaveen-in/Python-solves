from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def recieve_data():
    name = request.form.get("name")
    password = request.form.get("password")
    print(f"Name: {name} and Password: {password}")
    return f"<h1> Thanks {name} for your password {password} </h1>"

if (__name__ == "__main__"):
    app.run(debug=True)