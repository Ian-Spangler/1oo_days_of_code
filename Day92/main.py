from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def extract_top_colors(image_path, top_n=10):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((200, 200))
    pixels = np.array(img).reshape(-1, 3)

    colors, counts = np.unique(pixels, axis=0, return_counts=True)
    indices = np.argsort(counts)[::-1][:top_n]

    top_colors = [(tuple(colors[i]), counts[i]) for i in indices]
    return top_colors


@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    image_url = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)
            image_url = path

            extracted = extract_top_colors(path)
            colors = [
                {
                    "rgb": color,
                    "hex": rgb_to_hex(color),
                    "count": count,
                }
                for color, count in extracted
            ]

    return render_template("index.html", colors=colors, image_url=image_url)


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
