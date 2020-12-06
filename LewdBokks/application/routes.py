from flask import request, render_template, make_response, Blueprint
from flask import current_app as app
from .models import User, db

database_bp = Blueprint(
    'database_bp', __name__,
    template_folder='templates',
    static_folder = 'static'
)

@database_bp.route('/loginvalidation', methods=['POST'])
def find_user():
    username = request.args.get('username')
    password = request.args.get('password')

    if username and password:
        does_user_exist = User.query.filter(User.username == username or User.password == password).first()
        if does_user_exist:
            return make_response(
                'found'
            )
            user_to_added = User(
                username = username,
                password = password
            )
            db.session.add(user_to_added)
            db.session.commit()
    return render_template('index.html')