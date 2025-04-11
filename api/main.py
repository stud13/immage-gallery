import os
from flask import Flask, request
import requests
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL='https://api.unsplash.com/photos/random'
UNSPLASH_KEY=os.environ.get("UNSPLASH_KEY", "")
DEBUG=bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
  raise EnvironmentError("UNSPLASH_KEY value is empty. Please check .env.local file and set the value")

app = Flask(__name__)
CORS(app)

# DEBUG SECTION #
app.config["DEBUG"] = DEBUG
#################

@app.route("/new-image")
def new_image():
  word = request.args.get("query")

  headers = {
    "Accept-Version" : "v1",
    "Authorization" : "Client-ID " + UNSPLASH_KEY
  }
  params = {"query" : word}

  res = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
  data = res.json()
  return data

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)