from flask import Blueprint, jsonify
from app.models import Home,db
from app.models import Image
from app.forms import AddHome

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

@home_routes.route('/sell',methods=['POST'])
def addhome():
    form = AddHome()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = Home()
        form.populate_obj(data)
        db.session.add(dara)
        db.session.commit()
        return home.to_dict()
        


