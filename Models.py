from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)

    def __init__(self,id,username, password):
        self.id=id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username




