from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name_input = StringField('name_input', validators=[DataRequired()])
    desc_input = StringField('desc_input', validators=[DataRequired()])
    image_input = FileField('image_input', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    price_input = DecimalField('price_input', validators=[DataRequired()])