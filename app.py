from flask import Flask, request, jsonify
from traceback import print_exc
from datetime import datetime
from scripts import edit, get
from geoip import geolite2
import settings

app = Flask(__name__, static_url_path="")

@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.route('/clicks', methods=['POST'])
def click():
    if request.method == 'POST':
        # Upload clicks and geo data to DB
        edit('AF')
        return jsonify({"message": "h"})

@app.route('/country', methods=['GET', 'POST'])
def country():
    if request.method == 'GET':
        match = geolite2.lookup(request.headers['X-Forwarded-For'])
        return jsonify({"countries": get(match.country)})
    elif request.method == 'POST':
        match = geolite2.lookup(request.headers['X-Forwarded-For'])
        if match is not None:
            edit(match.country)
            return jsonify({"message": "+1!"}), 200
        else:
            return jsonify({"message": "Origin IP country wasn't found."}), 500

@app.route('/country/<string:cc>', methods = ['GET', 'POST'])
def country_specific(cc):
    if request.method == "GET":
        return jsonify({"stats": {
            "country": get(cc)[-3],
            "code": get(cc)[-2],
            "clicks": get(cc)[-1]
        }}), 200
    else:
        return "Method not allowed", 405
    
if __name__ == "__main__":
    app.run(debug = True)