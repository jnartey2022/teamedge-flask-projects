
from flask import Flask, render_template, request, json, jsonify, current_app as app, request
import os

import requests

app = Flask(__name__)
json_info = ' '
artist_path = os.path.join(app.static_folder, 'data', 'artist.json')
with open(artist_path, 'r'), as raw_json:
    json_info = json.load(raw_json)
@app.route('/')
def index():
    return 'Hello Team Edge! Flask server is up and running. This week is API practice.'

@app.route('/api/v1/artist/all', methods=['GET'])
def api_albums_all():
    #using with allows fore opening and closing of file
    with open(artist_data, 'r') as jsondata:
        artist = json.load(jsondata)
        #no need to return html template
        return jsonify(artist)


# @app.route('/about')
# def about():
#     return '<h1>About</h1><p>More content</p>'
# @app.route('/nasa')
# def show_nasa_pic():
#     today =str(date.today())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
