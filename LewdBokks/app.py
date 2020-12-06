from flask import Flask, request, render_template, redirect, url_for, g
from pymongo import MongoClient
from jinja2 import Environment, FileSystemLoader
import config
import json

code = config.db_password
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(
            "mongodb+srv://bobitybo:" + code + "@cluster0.rtdkg.mongodb.net/ISSProject?retryWrites=true&w=majority")


connection = Connect.get_connection()
db = connection["ISSProject"]
col = db["Fashion"]


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    error = None
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        if request.form['username'] != 'peter' or request.form['password'] != 'pedigrew':
            error = 'Invalid'
        else:
            return redirect(url_for('index'))
    return render_template("login.html", error=error)


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/preferences/')
def preferences():
    entries = {}
    dbs = db.list_collection_names()
    for datab in dbs:
        collec = db[datab]
        listy = []
        for x in collec.find_one():
            listy.append(x)
        entries[datab] = listy
    return render_template("preferences.html", entries=entries)


@app.route('/products/')
def products():
    return render_template("products.html")


@app.route('/insert', methods=['POST'])
def insert_to_db():
    content = request.json
    if request.method == 'POST':
        col.insert(json.loads(content))
    return "Received"


if __name__ == "__main__":
    app.run(debug=True)
