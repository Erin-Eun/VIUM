from project import db

# Manager Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
