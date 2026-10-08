from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ---------------------------- MODEL ------------------------------- #
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=True)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

# ---------------------------- ROUTES ------------------------------- #
@app.route("/posts", methods=["GET"])
def get_all_posts():
    posts = Post.query.all()
    return jsonify(posts=[post.to_dict() for post in posts])

@app.route("/post/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify(post=post.to_dict())
    return jsonify(error="Post not found"), 404

@app.route("/add", methods=["POST"])
def add_post():
    data = request.get_json()
    new_post = Post(
        title=data["title"],
        subtitle=data.get("subtitle", ""),
        body=data["body"],
        author=data["author"]
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify(success="Post added"), 201

@app.route("/update/<int:post_id>", methods=["PATCH"])
def update_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify(error="Post not found"), 404
    data = request.get_json()
    post.title = data.get("title", post.title)
    post.subtitle = data.get("subtitle", post.subtitle)
    post.body = data.get("body", post.body)
    post.author = data.get("author", post.author)
    db.session.commit()
    return jsonify(success="Post updated")

@app.route("/delete/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify(error="Post not found"), 404
    db.session.delete(post)
    db.session.commit()
    return jsonify(success="Post deleted")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)