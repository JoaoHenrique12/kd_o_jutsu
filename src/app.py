from flask import Flask, render_template, request
from .utils import search_jutsu_df_by_name, append_seal_sequence

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/jutsu_by_name")
def search_jutsu_by_name():
    search_query = request.args.get('search_query', '')

    jutsus_found = search_jutsu_df_by_name(search_query)
    jutsus_found = append_seal_sequence(jutsus_found)
    return render_template('search_jutsu_by_name.html', jutsus=jutsus_found)

@app.route("/jutsu_by_seals")
def search_jutsu_by_seals():
    return "We are working on it.(Seals)"
