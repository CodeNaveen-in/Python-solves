from flask import Flask
from random import randint
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Guess a number between 0 and 9 </h1> /" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

v1 = randint(1,10) ### By random module
v2 = 7 ### By Hard Coded
#v3 = int(input("Enter the int:\t")) ### By asking user
var = v1

@app.route("/<int:guess>")
def num_check(guess):
    if (guess == var):
        return "<h2 style = 'text-align: center; color: green'> You FOUND me! </h1>"\
        "<img src= 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif (guess > var):
        return "<h2 style = 'color: purple'> TOO HIGH Tr Again! </h1>"\
        "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if (guess < var):
        return "<h2 style = 'color: red'> TOO LOW Try Again! </h1>"\
        "<img src= 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

if (__name__ == "__main__"):
    app.run(debug=True)