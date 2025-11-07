from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

def get_top_colors(image_path, num_colors=5):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((100, 100))  # Speed up processing
    pixels = list(img.getdata())
    most_common = Counter(pixels).most_common(num_colors)
    return most_common

@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    if request.method == "POST":
        file = request.files["image"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            colors = get_top_colors(filepath)
    return render_template("index.html", colors=colors)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)