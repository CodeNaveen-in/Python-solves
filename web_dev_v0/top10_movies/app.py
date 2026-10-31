from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = "movies.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                rating REAL,
                poster_url TEXT
            )
        """)

init_db()

@app.route("/")
def index():
    with sqlite3.connect(DB) as conn:
        movies = conn.execute("SELECT * FROM movies ORDER BY rating DESC LIMIT 10").fetchall()
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        rating = request.form["rating"]
        poster_url = request.form["poster_url"]
        with sqlite3.connect(DB) as conn:
            conn.execute("INSERT INTO movies (title, description, rating, poster_url) VALUES (?, ?, ?, ?)",
                         (title, description, rating, poster_url))
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    with sqlite3.connect(DB) as conn:
        movie = conn.execute("SELECT * FROM movies WHERE id = ?", (movie_id,)).fetchone()
    if request.method == "POST":
        new_rating = request.form["rating"]
        with sqlite3.connect(DB) as conn:
            conn.execute("UPDATE movies SET rating = ? WHERE id = ?", (new_rating, movie_id))
        return redirect(url_for("index"))
    return render_template("edit.html", movie=movie)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)