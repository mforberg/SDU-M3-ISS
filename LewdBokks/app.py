from flask import Flask, request, render_template, redirect, url_for, session
from backend.db import *
import json
from forms import *
import os
from backend.database_connection import DatabaseConnection
from flask_session import Session
from backend.lootboxes import LootBox

secret_key = os.urandom(32)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = secret_key
app.config['SESSION_TYPE'] = "filesystem"
Session(app)
dbc = DatabaseConnection().get_instance()
lb = LootBox().get_instance()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    error = None
    form = LoginForm()
    if request.method == 'POST':
        result = dbc.super_secure_credentials(request.form['username'])
        if result:
            if 'CUSTOMER' in result:
                if request.form['password'] == result['CUSTOMER'][2]:
                    session['uuid'] = result['CUSTOMER'][0]
                    session['username'] = result['CUSTOMER'][1]
                    session['customer'] = True
                    return redirect(session['referer'])
                else:
                    error = 'Invalid'
            elif 'BUSINESS' in result:
                if request.form['password'] == result['BUSINESS'][2]:
                    session['uuid'] = result['BUSINESS'][0]
                    session['username'] = result['BUSINESS'][1]
                    session['customer'] = False
                    session['business'] = True
                    return redirect(session['referer'])
                else:
                    error = 'Invalid'
    return render_template("login.html", error=error, form=form)


@app.route('/login')
def login():
    form = LoginForm()
    session['referer'] = request.environ['HTTP_REFERER']
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('uuid')
    session.pop('customer')
    if 'business' in session:
        session.pop('business')
    return redirect(url_for('index'))

@app.route('/emergencysessionclear')
def nukeem():
   session.clear()
   [session.pop(key) for key in list(session.keys())]
   return redirect(url_for('index'))

@app.route('/register')
def register():
    form = RadioChoiceForm()
    return render_template('register.html', form=form)


@app.route('/validateChoice', methods=["POST"])
def validate_choice():
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


@app.route('/validateRegistrationPerson', methods=["POST", "GET"])
def validate_registration_person():
    error = None
    form = RegisterPersonForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        username_dict = dbc.get_instance().get_user_names(username)
        email_dict = dbc.get_instance().get_emails(email)
        if len(username_dict) > 0:
            error = 'username taken'
        elif len(email_dict) > 0:
            error = 'email taken'
        elif password != request.form['confirm']:
            error = 'Passwords does not match'
        else:
            dbc.get_instance().register_person(username, password, email)
            return redirect(url_for('index'))
    return render_template("registerPerson.html", error=error, form=form)


@app.route('/validateRegistrationCompany', methods=["POST", "GET"])
def validate_registration_company():
    error = None
    form = RegisterCompanyForm()
    if request.method == 'POST':
        username = request.form['username']
        company_name = request.form['companyname']
        url = request.form['websiteurl']
        password = request.form['password']
        username_dict = dbc.get_instance().get_user_names(username)
        company_name_dict = dbc.get_instance().get_company_names(company_name)
        if len(username_dict) > 0:
            error = 'username taken'
        elif len(company_name_dict) > 0:
            error = 'company name taken'
        elif password != request.form['confirm']:
            error = 'Passwords does not match'
        else:
            dbc.get_instance().register_company(company_name, url, username, password)
            return redirect(url_for('index'))
    return render_template("registerCompany.html", error=error, form=form)


@app.route('/preferences/')
def preferences():
    unique_categories = dbc.get_distinct_categories()
    uuid = session['uuid']
    pref_list = dbc.get_preferences(uuid)
    prime_entries = {}
    secondary_entries = {}

    for category in unique_categories[0]:
        if category in pref_list:
            prime_entries[category] = True
        else:
            prime_entries[category] = False
    for category in unique_categories[1]:
        if category in pref_list:
            secondary_entries[category] = True
        else:
            secondary_entries[category] = False

    return render_template("preferences.html", prime_entries=prime_entries, secondary_entries=secondary_entries)


@app.route('/coupons/', methods=['GET', 'POST'])
def coupons():
    if 'uuid' in session:
        b_uuid = session['uuid']
    else:
        raise Exception("Oof")
    categories = dbc.get_distinct_categories()
    form = DeleteCoupon()
    form2 = AddCoupon(primary_cat=categories[0], sub_cat=categories[1])
    records = dbc.get_coupons_by_uuid(b_uuid)
    error = None

    return render_template("coupons.html", entries=records, form=form, addform=form2, error=error)


@app.route('/delcoupon/', methods=['POST'])
def del_coupon():
    if 'uuid' in session:
        b_uuid = session['uuid']
    else:
        raise Exception("Oof")
    if request.method == "POST":
        if request.form['uuid_name']:
            dbc.delete_coupon_by_uuids(b_uuid, request.form['uuid_name'])
            return redirect(url_for('coupons'))


@app.route('/addcoupon/', methods=['POST'])
def add_coupon():
    if 'uuid' in session:
        b_uuid = session['uuid']
    else:
        raise Exception("Oof")
    if request.method == "POST":
        if request.form['price']:
            dbc.add_coupon(b_uuid, request.form)
            return redirect(url_for('coupons'))


@app.route('/products/')
def products():
    uber_banger_list_of_uuid = []

    if "username" in session:
        uuid = dbc.get_uuid_from_username(session["username"])[0]
        pref_list = dbc.get_preferences(uuid)

        uuid_list = dbc.get_products_given_preferences(pref_list)
        for uuid in uuid_list:
            for listuuid in uuid:
                uber_banger_list_of_uuid.append(listuuid[0])
    else:
        product_list = dbc.get_products()
        return render_template("products.html", uuids=uber_banger_list_of_uuid)
    return render_template("products.html", uuids=uber_banger_list_of_uuid)


@app.route('/lootbox', methods=['POST', 'GET'])
def loot_box():
    form = BuyLootBox()
    if 'uuid' in session:
        user_uuid = session['uuid']
        if request.method == 'POST':

            lootbox_type = request.form['payment']
            discount, item, discount_code = lb.generate_lootbox(user_uuid, dbc, lootbox_type)
            session['discount'] = discount
            session['item'] = item
            session ['code'] = discount_code
            return redirect(url_for('purchase'))     

        return render_template("lootBox.html", form = form, entries = user_uuid)

    else:
        return render_template("lootBox.html", form = form)


@app.route('/purchase')
def purchase():
    if 'discount' in session:
        discount = session.pop('discount')
        item = session.pop('item')
        discount_code = session.pop('code')
        return render_template("purchase.html", reward = discount, name = item, code = discount_code)
    return render_template("purchase.html")

@app.route('/myloot')
def myloot():
    if 'uuid' in session:
        user = session['uuid']
        lootboxes = dbc.get_lootboxes(user)
        return render_template("myloot.html", entries = lootboxes)

@app.route('/update_prefs', methods=["POST"])
def update_prefs():
    uuid = session["uuid"]
    pref_list = []
    for key in request.form:
        pref_list.append(key)
    dbc.update_users_preferences(uuid, pref_list)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
