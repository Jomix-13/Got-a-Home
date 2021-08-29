from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,SelectField,IntegerField,TextField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Question

class QuestionForm(FlaskForm):

    question = StringField('Ask Question', validators=[DataRequired()])
    homeId = IntegerField('homeId', validators=[DataRequired()])
    
