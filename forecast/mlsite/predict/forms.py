# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired

class PredictForm(FlaskForm):
    # sharedfile.fieldsClass
    field1 = StringField('field one',validators=[DataRequired()])
    field2 = StringField('field two',validators=[DataRequired()])
    submit = SubmitField("predict")
