from app import db
# from flask.ext.admin.contrib.sqla import ModelView

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    father_name = db.Column(db.String(64))
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(8), index=True)

# class MyModelView(ModelView):
#     form_overrides = dict(
#         sex=SelectField
#     )
#     form_args = dict(
#         sex=dict(
#             choices=[
#                 ('man', 'M'),
#                 ('women', 'Z')
#             ]
#         )
#     )
#     def __init__(self):
#         super(MyModelView, self).__init__(Customer, db.session)
