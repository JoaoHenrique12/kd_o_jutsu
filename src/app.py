from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route("/point_and_click")
def point_and_click():
    return "We are working on it."
