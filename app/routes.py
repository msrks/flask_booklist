from flask import render_template, redirect
from app import app, db
from app.models import Book
from app.forms import BookForm


@app.route('/', methods=['GET', 'POST'])
def list_books():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        price = form.price.data
        form.title.data = ''
        form.price.data = 0

        book = Book(title=title, price=price)
        db.session.add(book)
        db.session.commit()

    books = Book.query.all()
    total_price = sum([i.price for i in books])
    return render_template('books_list.html', form=form, books=books, total_price=total_price)


@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return redirect('/')

    db.session.delete(book)
    db.session.commit()
    return redirect('/')
