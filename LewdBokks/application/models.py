from . import db

class User(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    username = db.Column(
        db.String(64),
        index = False,
        unique = True,
        nullable = False
    )

    password = db.Column(
        db.String(80),
        index = False,
        nullable = False
    )