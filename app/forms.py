from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('title:', validators=[DataRequired()])
    price = IntegerField('price:', validators=[DataRequired()])
    # when_added = DateTimeField('datetime:')
    who_added = StringField('your name:')
    submit = SubmitField('Submit')
