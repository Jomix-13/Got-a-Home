from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,SelectField,IntegerField,TextField,validators
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Question

class QuestionForm(FlaskForm):

    question = StringField('Ask Question', [validators.Length(min=4, max=100)])
    # validators=[DataRequired(),Length(min=4, max=25),message= 'min 4 char max 25']])
    homeId = IntegerField('homeId', validators=[DataRequired()])
    
