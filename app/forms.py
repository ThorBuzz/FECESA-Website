from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, NumberRange, Length
from flask_wtf.file import FileAllowed

class ProductForm(FlaskForm):
    title = StringField('Product Title', validators=[
        DataRequired(),
        Length(min=5, max=100)
    ])
    description = TextAreaField('Description', validators=[
        Length(max=500)
    ])
    price = DecimalField('Price', validators=[
        DataRequired(),
        NumberRange(min=0.01)
    ])
    category = SelectField('Category', choices=[
        ('textbooks', 'Textbooks'),
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('services', 'Services')
    ], validators=[DataRequired()])
    condition = SelectField('Condition', choices=[
        ('new', 'Brand New'),
        ('used', 'Used - Like New'),
        ('good', 'Used - Good')
    ], validators=[DataRequired()])
    images = FileField('Product Images', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])