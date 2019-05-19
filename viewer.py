from flask import Flask
from flask import render_template
import pickle

with open('videos.data', 'rb') as f:
    videos = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def view():
    return render_template('view.html', videos=videos)
