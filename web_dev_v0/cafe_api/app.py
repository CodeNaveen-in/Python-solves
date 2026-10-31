from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

API_KEY = "TopSecretAPIKey"

# ---------------------------- MODEL ------------------------------- #
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    map_url = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    seats = db.Column(db.String(20), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(10), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# ---------------------------- ROUTES ------------------------------- #
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = Cafe.query.all()
    cafe = random.choice(cafes)
    return jsonify(cafe=cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search", methods=["GET"])
def search_cafe():
    loc = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=loc).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    return jsonify(error={"Not Found": "No cafe at that location"}), 404

@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.form
    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=bool(int(data["has_toilet"])),
        has_wifi=bool(int(data["has_wifi"])),
        has_sockets=bool(int(data["has_sockets"])),
        can_take_calls=bool(int(data["can_take_calls"])),
        coffee_price=data["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe added successfully"}), 201

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Price updated")
    return jsonify(error="Cafe not found"), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(error="Unauthorized"), 403
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success="Cafe deleted")
    return jsonify(error="Cafe not found"), 404

if __name__ == "__main__":
    app.run(debug=True)