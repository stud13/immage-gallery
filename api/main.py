import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client

gallery = mongo_client.gallery
images_collection = gallery.images

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError(
        "UNSPLASH_KEY value is empty. Please check .env.local file and set the value"
    )

app = Flask(__name__)
CORS(app)

# DEBUG SECTION #
app.config["DEBUG"] = DEBUG
#################


@app.route("/new-image")
def new_image():
    """Sends request to Unsplash api and returns a new image"""
    word = request.args.get("query")

    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + UNSPLASH_KEY}
    params = {"query": word}

    res = requests.get(url=UNSPLASH_URL, headers=headers, params=params, timeout=10)
    data = res.json()
    return data


@app.route("/images", methods=["GET", "POST"])
def images():
    """GET/POST endpoint to get images from server and load images to server"""
    if request.method == "GET":
        # read images from the database
        images = images_collection.find({})
        return jsonify([img for img in images])
    if request.method == "POST":
        # add image to the database
        image = request.get_json()
        image["_id"] = image.get("id")
        result = images_collection.insert_one(image)
        inserted_id = result.inserted_id
        return {"inserted_id": inserted_id}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
