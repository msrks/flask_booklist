from flask import Flask
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret' # CSRF対策でtokenの生成に必要
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

class BookForm(FlaskForm):
    title = StringField('title:', validators=[DataRequired()])
    price = IntegerField('price:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def list_books():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        price = form.price.data
        form.title.data = ''
        form.price.data = 0

        book = Book(title, price)
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
