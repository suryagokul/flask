from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = "sqlite:///relationship.db"

# instantiating
db =SQLAlchemy(app)

# one to many relationship 

# like one person can borrow multiple books and one book can owns one owner/person.

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	books = db.relationship('Books', backref='owner')

	def __repr__(self):
		return f"Person('{self.name}')"


class Books(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_name = db.Column(db.String(60), nullable=False)
	owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

	def __repr__(self):
		return f"Books('{self.book_name}', '{self.owner_id}')"



