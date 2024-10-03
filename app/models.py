from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

#db = SQLAlchemy()

# Model autora
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', secondary='author_book', back_populates='authors')

    def __str__(self):
       return f"<Author {self.name}>"

# Model książki
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    is_on_shelf = db.Column(db.Boolean, default=True)
    authors = db.relationship('Author', secondary='author_book', back_populates='books')
    loans = db.relationship('Loan', back_populates='book')

    def __str__(self):
       return f"<Book {self.title}>"

# Tabela many-to-many dla książek i autorów
author_book = db.Table('author_book',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

# Model wypożyczeń
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(100), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', back_populates='loans')

    def __str__(self):
       return f"<Loan {self.borrower}, Book: {self.book.title}>"
