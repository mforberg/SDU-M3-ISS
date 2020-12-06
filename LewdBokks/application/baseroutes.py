from flask import Flask, request, render_template, redirect, url_for, Blueprint
from backend.db import *
import json
from application.forms import LoginForm

base_bp = Blueprint(
    'base_bp', __name__,
    template_folder='templates',
    static_folder = 'static'
)

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


@base_bp.route('/')
def index():
    return render_template("index.html")


@base_bp.route('/validate', methods=['GET', 'POST'])
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


@base_bp.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('index.html')
    return render_template('login.html', form=form)


@base_bp.route('/preferences/')
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


@base_bp.route('/products/')
def products():
    return render_template("products.html")


@base_bp.route('/insert', methods=['POST'])
def insert_to_db():
    content = request.json
    if request.method == 'POST':
        #con.get_table("Fashion").insert(json.loads(content))
        #TODO: fix this ^ is original line, but con no work
        pass
    return "Received"


if __name__ == "__main__":
    app.run(debug=True)
