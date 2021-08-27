from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,SelectField,IntegerField,TextField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Home

states =[
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]

options = ["For Sale","For Rent","Pending Sale"]

class HomeForm(FlaskForm):
    price = DecimalField('Price', validators=[DataRequired()])
    stAddress = StringField('Street Address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = SelectField('Street Address', choices=states)
    zipCode = IntegerField('Zip Code', validators=[DataRequired()])
    latitude = DecimalField('Latitude', validators=[DataRequired()])
    longitude = DecimalField('Longitude', validators=[DataRequired()])
    lotSize = IntegerField('Lot Size', validators=[DataRequired()])
    beds = IntegerField('No. Beds', validators=[DataRequired()])
    bath = IntegerField('No. Bath', validators=[DataRequired()])
    status = SelectField('Status', choices=options)
    image = TextField('Image', validators=[DataRequired()])
    
