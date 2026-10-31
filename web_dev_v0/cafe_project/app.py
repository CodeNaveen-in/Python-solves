from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import CafeForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        cafes = list(reader)
    return render_template("cafes.html", cafes=cafes)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_data = [form.name.data, form.location.data, form.open_time.data,
                    form.close_time.data, form.coffee_rating.data,
                    form.wifi_rating.data, form.power_rating.data]
        with open("cafe-data.csv", mode="a", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_data)
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)