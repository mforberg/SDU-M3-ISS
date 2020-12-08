from flask import Flask, request, render_template, redirect, url_for
from backend.db import *
import json
from forms import *
import os
from backend.database_connection import DatabaseConnection

secret_key = os.urandom(32)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = secret_key
dbc = DatabaseConnection().get_instance()


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
    return render_template('login.html', form=form)


@app.route('/register')
def register():
    form = RadioChoiceForm()
    return render_template('register.html', form=form)


@app.route('/validateChoice', methods=["POST"])
def validatechoice():
    form = RadioChoiceForm()
    print(request.form)
    if request.form['radio'] == 'company':
        return redirect(url_for('company'))
    else:
        return redirect(url_for('person'))


@app.route('/register/person', methods=["POST", "GET"])
def person():
    form = RegisterPersonForm()
    return render_template('registerPerson.html', form=form)


@app.route('/register/company', methods=["POST", "GET"])
def company():
    form = RegisterCompanyForm()
    return render_template('registerCompany.html', form=form)


@app.route('validateRegistration', methods=["POST", "GET"])
def validateregistration():


# @app.route('/register/X')
# def registerx():
#     print(request)
#     x = request.form["person"]
#     if x:
#         print("dakpo")
#     return render_template('register.html')


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
    uuid = 'b3089a02-d258-4ba2-a90a-3752432e2892'
    records = dbc.get_instance().get_coupons_by_uuid(uuid)

    return render_template("coupons.html", entries=records)


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
def loot_box():
    return render_template("lootBox.html")


if __name__ == "__main__":
    app.run(debug=True)
