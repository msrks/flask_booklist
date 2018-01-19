from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('title:', validators=[DataRequired()])
    price = IntegerField('price:', validators=[DataRequired()])
    submit = SubmitField('Submit')
