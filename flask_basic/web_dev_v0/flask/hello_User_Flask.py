from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "The server has started: \nFor your name add username/<yourname> in path"

# Adding Variable to the URL
@app.route("/username/<name>/<int:number>")
def user_hello(name, number):
    return f"Hello dear user {name}. Welcome to Site!, You are {number} years old!"

#Adding HTML & CSS to the URL
@app.route("/html")
def html_code():
    return "<h1> Haha Hello </h1> <hr> <p> This is one mini para </p>"

@app.route("/css")
def css_code():
    return "<h1 style= 'text-align: center; color: blue'> Haha Hello </h1> <hr> <p style= 'text-align: center; color: Green; padding: 20px'> This is one mini para </p>"

if (__name__ == "__main__"):
    app.run(debug=True)