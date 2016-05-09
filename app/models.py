from app import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    father_name = db.Column(db.String(64))
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(8), index=True)
    phone_number = db.Column(db.String(16))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    diseases = db.relationship('Disease',
                               backref='patient',
                               lazy='dynamic'
                               )


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    father_name = db.Column(db.String(64))
    patients = db.relationship('Patient',
                               backref='doctor',
                               lazy='dynamic'
                               )
    admin = db.Column(db.Boolean, default=True)


class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
