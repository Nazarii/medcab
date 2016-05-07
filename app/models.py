from app import db


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    father_name = db.Column(db.String(64))
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(8), index=True)
