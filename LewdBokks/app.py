from flask import Flask, request, render_template, redirect, url_for
from backend.db import *
import json
from forms import LoginForm
import os

secret_key = os.urandom(32)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = secret_key


# class Connect(object):
#     @staticmethod
#     def get_connection():
#         return MongoClient(
#             "mongodb+srv://bobitybo:" + code + "@cluster0.rtdkg.mongodb.net/ISSProject?retryWrites=true&w=majority")
#
#
# connection = Connect.get_connection()
# db = connection["ISSProject"]
# col = db["Fashion"]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    error = None
    form = LoginForm()
    print(request.method)
    if request.method == 'POST':
        print(request.form)
        if request.form['username'] != 'peter' or request.form['password'] != 'pedigrew':
            error = 'Invalid'
        else:
            return redirect(url_for('index'))
    return render_template("login.html", error=error, form=form)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('index.html')
    return render_template('login.html', form=form)


@app.route('/register')
def register():
    return render_template('index.html')


@app.route('/preferences/')
def preferences():
    entries = {}
    temp = get_db()
    dbs = temp.list_collection_names()
    for datab in dbs:
        collec = temp[datab]
        listy = []
        for x in collec.find_one():
            listy.append(x)
        entries[datab] = listy
    return render_template("preferences.html", entries=entries)

@app.route('/coupons/')
def coupons():
    return render_template("coupons.html")

@app.route('/products/')
def products():
    return render_template("products.html")


@app.route('/insert', methods=['POST'])
def insert_to_db():
    content = request.json
    if request.method == 'POST':
        # con.get_table("Fashion").insert(json.loads(content))
        # TODO: fix this ^ is original line, but con no work
        pass
    return "Received"

@app.route('/lootBox')
def lootBox():
    return render_template("lootBox.html")

if __name__ == "__main__":
    app.run(debug=True)
