from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import pandas as pd

app = Flask(__name__)
CORS(app)
# app.config["DEBUG"] = True

# model = load('smallerbad.pkl')
@app.route('/')
def home():
    title = request.args['title']
    body = request.args['body']
    body = [body]
    md = load("alg.sav")
    rt = md.predict(body)
    rt = str(rt)
    return(rt)

# app.run()
# or run with gunicorn api:app
        # We'll use apache2 ^^^
