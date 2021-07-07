# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField, SelectField
from wtforms.validators import DataRequired, Required

class PredictForm(FlaskForm):
    # sharedfile.fieldsClass
    parents_educ_options = [ ( 1,"some high school"), (1,"high school") , (2,"some college") ,( 2,"associate's degree"),(3,"bachelor's degree"), (4,"master's degree")] 
                 
    gender = SelectField('Gender', choices = [ (1,'female'), (2,'male')], validators = [Required()])
    parental__education = SelectField('Parental level of education', choices = parents_educ_options,validators=[DataRequired()])
    lunch = RadioField('lunch',choices=[ ('1','standard'),('0','free/reduced')],validators=[DataRequired()])
    submit = SubmitField("predict")

    def getValues(self):
      return [self.gender.data , self.parental__education.data, self.lunch.data] 
      