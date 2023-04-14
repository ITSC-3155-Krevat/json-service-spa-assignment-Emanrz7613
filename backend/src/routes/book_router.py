from flask import Blueprint

book_router = Blueprint('books', __name__, url_prefix='/books')


@book_router.get('')
def get_all_books():
    pass


@book_router.get('/<int:book_id>')
def get_single_book(book_id: int):
    pass


@book_router.post('')
def create_book():
    pass


@book_router.put('/<int:book_id>')
def update_book(book_id: int):
    pass


@book_router.delete('/<int:book_id>')
def delete_book(book_id: int):
    pass
