
# show book list
from app.model.book import Book


def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)




