from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,SelectField,IntegerField,TextField,validators
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
    price = IntegerField('Price', [validators.NumberRange(min=100000, max=100000000,message='is more than 100k and less than 100m')])
    stAddress = StringField('Street Address', [validators.Length(min=4, max=25)])
    city = StringField('city', [validators.Length(min=4, max=25)])
    state = SelectField('Street Address', choices=states)
    zipCode = IntegerField('Zip Code', [validators.NumberRange(min=11111, max=99999,message=' is 5 digits')])
    latitude = DecimalField('Latitude', [validators.NumberRange(min=-90, max=90,message='range is -90 to 90')])
    longitude = DecimalField('Longitude', [validators.NumberRange(min=-180, max=180,message='range is -180 to 180')])
    lotSize = IntegerField('Lot Size', [validators.NumberRange(min=3000, max=42000,message='range is 3000 to 42000 sq ft')])
    beds = IntegerField('No. Beds', [validators.NumberRange(min=1, max=99)])
    bath = IntegerField('No. Bath', [validators.NumberRange(min=1, max=99)])
    status = SelectField('Status', choices=options)
    image = TextField('Image', [validators.URL(require_tld=False, message=None)])
    
