from flask import Flask, request, render_template, redirect, url_for
from backend.db import *
import json
from forms import LoginForm, DeleteCoupon, AddCoupon
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
    if form.validate_on_submit():
        return render_template('index.html')
    return render_template('login.html', form=form)


@app.route('/register')
def register():
    return render_template('register.html')


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


#b_uuid = 'b3089a02-d258-4ba2-a90a-3752432e2892'


@app.route('/coupons/', methods=['GET', 'POST'])
def coupons():
    b_uuid = 'b3089a02-d258-4ba2-a90a-3752432e2892'
    categories = dbc.get_distinct_primary_categories()
    form2 = AddCoupon(primary_cat=categories[0], sub_cat=categories[1])

    records = dbc.get_coupons_by_uuid(b_uuid)
    error = None
    form = DeleteCoupon()
    # if request.method == "POST":
    #     if request.form['uuid_name']:
    #         print(b_uuid)
    #         print(request.form['uuid_name'])
    #         dbc.delete_coupon_by_uuids(b_uuid, request.form['uuid_name'])
    #         return redirect(url_for('coupons'))
    return render_template("coupons.html", entries=records, form=form, addform=form2, error=error)


@app.route('/delcoupon/', methods=['POST'])
def del_coupon():
    b_uuid = 'b3089a02-d258-4ba2-a90a-3752432e2892'
    if request.method == "POST":
        if request.form['uuid_name']:
            dbc.delete_coupon_by_uuids(b_uuid, request.form['uuid_name'])
            return redirect(url_for('coupons'))


@app.route('/addcoupon/', methods=['POST'])
def add_coupon():
    b_uuid = 'b3089a02-d258-4ba2-a90a-3752432e2892'
    if request.method == "POST":
        if request.form['price']:
            dbc.add_coupon(b_uuid, request.form)
            return redirect(url_for('coupons'))


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
