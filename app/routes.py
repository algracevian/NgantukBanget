from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# Home Page
@main.route('/')
def home():
    return render_template('home.html')

# List Buku
@main.route('/books')
def books():
    # Contoh data buku
    book_list = [
        {"title": "Buku 1", "author": "Penulis A", "year": 2020},
        {"title": "Buku 2", "author": "Penulis B", "year": 2021},
        {"title": "Buku 3", "author": "Penulis C", "year": 2022},
    ]
    return render_template('books.html', books=book_list)
