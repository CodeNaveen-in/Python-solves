from flask import Flask

app = Flask(__name__)

# Decorators that wrap and modify HTML output
def bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def hello():
    return "<h1 style='text-align: center'>WELCOME TO SERVER</h1>"

@app.route("/magic")
@bold
@italic
@underline
def magic():
    return "<p style='text-align: center; margin: 50%'>WELCOME TO SERVER</p>"

if __name__ == "__main__":
    app.run(debug=True)