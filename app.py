from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login")
def login():
    return render_template("index.html")