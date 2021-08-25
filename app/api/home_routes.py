from flask import Blueprint, jsonify
from app.models import Home
from app.models import Image

home_routes = Blueprint('homes', __name__)


@home_routes.route('/')
def allhomes():
    homes = Home.query.join(Image).all()
    print ('>>>>>>>>>>>>',homes)
    return {'homes': [home.to_dict() for home in homes]}
