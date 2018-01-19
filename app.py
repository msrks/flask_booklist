from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return '<title %s>' % self.title


@app.route('/')
def books_list():
    books = Book.query.all()
    total_price = sum([i.price for i in books])
    return render_template('books_list.html', books=books, total_price=total_price)


@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    price = request.form['price']
    if not title or not price:
        return 'Error'

    try:
        price = int(price)
    except:
        return 'Error'

    book = Book(title, price)
    db.session.add(book)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return redirect('/')

    db.session.delete(book)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
