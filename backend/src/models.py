from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):

    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, title: str, author: str, rating: int) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self) -> str:
        return f'Book({self.title}, {self.author}, {self.rating})'
