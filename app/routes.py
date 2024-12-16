from flask import Blueprint, render_template, request, redirect, url_for, current_app

main = Blueprint('main', __name__)

# Home Page
@main.route('/')
def home():
    return render_template('home.html')

# List Books (Read)
@main.route('/books')
def books():
    cur = current_app.mysql.connection.cursor()  # Access MySQL connection from current_app
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    return render_template('books.html', books=books)

# Create Book (Create)
@main.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        cur = current_app.mysql.connection.cursor()  # Access MySQL connection from current_app
        cur.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
        current_app.mysql.connection.commit()
        cur.close()

        return redirect(url_for('main.books'))

    return render_template('add_book.html')

# Edit Book (Update)
@main.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    cur = current_app.mysql.connection.cursor()  # Access MySQL connection from current_app
    cur.execute("SELECT * FROM books WHERE id = %s", [id])
    book = cur.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        cur.execute("UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s", (title, author, year, id))
        current_app.mysql.connection.commit()
        cur.close()

        return redirect(url_for('main.books'))

    cur.close()
    return render_template('edit_book.html', book=book)

# Delete Book (Delete)
@main.route('/books/delete/<int:id>')
def delete_book(id):
    cur = current_app.mysql.connection.cursor()  # Access MySQL connection from current_app
    cur.execute("DELETE FROM books WHERE id = %s", [id])
    current_app.mysql.connection.commit()
    cur.close()

    return redirect(url_for('main.books'))
