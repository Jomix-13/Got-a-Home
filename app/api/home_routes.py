from flask import Blueprint, jsonify
from app.models import Home
from app.models import Image

home_routes = Blueprint('homes', __name__)


@home_routes.route('/')
def allhomes():
    homes = Home.query.all()
    return {'homes': [home.to_dict() for home in homes]}


@home_routes.route('/<int:id>')
def onehome(id):
    home = Home.query.get(id)
    print ('>>>>>>>>>>>>',home)
    return home.to_dict()
