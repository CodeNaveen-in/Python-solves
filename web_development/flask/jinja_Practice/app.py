from flask import Flask, render_template
from random import randint
import datetime
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)

ran_num = randint(1,10)
date = datetime.date.today()
name = "Naveen Garg"
gen_api = os.getenv("GENDERISE_API")
agi_api = os.getenv("AGIFY_API")

@app.route("/")
def hello():
    return render_template("index.html", num=ran_num, date=date, name=name)

@app.route("/guess/<name>")
def guess(name):
    gen_url = requests.get(gen_api+name)
    agi_url = requests.get(agi_api+name)
    gen_data = gen_url.json()
    age_data = agi_url.json()
    name = gen_data["name"]
    age = age_data["age"]
    gender = gen_data["gender"]
    return render_template("guess.html", jin_name=name, jin_age=age, jin_gender = gender)

@app.route("/blog")
def blog():
    blog_url = os.getenv("BLOGPOST_API")
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("blog.html", posts=blog_data)

if (__name__ == "__main__"):
    app.run(debug=True)