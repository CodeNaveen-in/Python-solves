from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = "books.db"

# ---------------------------- DB INIT ------------------------------- #
def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                rating REAL
            )
        """)

init_db()

# ---------------------------- ROUTES ------------------------------- #
@app.route("/")
def index():
    with sqlite3.connect(DB) as conn:
        books = conn.execute("SELECT * FROM books").fetchall()
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        with sqlite3.connect(DB) as conn:
            conn.execute("INSERT INTO books (title, author, rating) VALUES (?, ?, ?)", (title, author, rating))
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    with sqlite3.connect(DB) as conn:
        book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if request.method == "POST":
        new_rating = request.form["rating"]
        with sqlite3.connect(DB) as conn:
            conn.execute("UPDATE books SET rating = ? WHERE id = ?", (new_rating, book_id))
        return redirect(url_for("index"))
    return render_template("edit.html", book=book)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    with sqlite3.connect(DB) as conn:
        conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)