from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
