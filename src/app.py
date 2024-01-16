from flask import Flask, render_template, request, url_for
from .utils import get_seal_name_by_id, search_jutsu_df_by_name, append_seal_sequence, search_jutsu_df_by_seals_id, get_seal_id_by_name

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/search_jutsu_by_name")
def search_jutsu_by_name():
    search_query = request.args.get('search_query', '')

    jutsus_found = search_jutsu_df_by_name(search_query)
    jutsus_found = append_seal_sequence(jutsus_found)
    return render_template('search_jutsu_by_name.html', jutsus=jutsus_found)

@app.route("/search_jutsu_by_seals")
def search_jutsu_by_seals():
    seals_names = list(map(get_seal_name_by_id, range(1,14)))
    links = [url_for('static', filename=f'images/seals/{name}_seal.webp') for name in seals_names]
    links = zip(links, seals_names)

    search_query = request.args.get('search_query', '')
    search_query = search_query[:-1]

    seals_id = []
    if search_query != '':
        seals_id = list(map(get_seal_id_by_name, search_query.split(',')))

    print(seals_id)

    jutsus_found = search_jutsu_df_by_seals_id(seals_id)
    jutsus_found = append_seal_sequence(jutsus_found)

    return render_template('search_jutsu_by_seals.html', image_links = links, jutsus = jutsus_found)
