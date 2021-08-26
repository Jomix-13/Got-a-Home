from flask import Blueprint, jsonify,request
from app.models import Home,db
from app.models import Image
from app.forms import AddHome
from flask_login import current_user

home_routes = Blueprint('homes', __name__)


@home_routes.route('/')
def allhomes():
    homes = Home.query.all()
    return {'homes': [home.to_dict() for home in homes]}


@home_routes.route('/<int:id>')
def onehome(id):
    home = Home.query.get(id)
    
    return home.to_dict()

@home_routes.route('/sell',methods=['POST'])
def addhome():
    form = AddHome()
    form['csrf_token'].data = request.cookies['csrf_token']
    print ('>>>>>>>>>>>>','1')
    if form.validate_on_submit():
        home = Home()
        form.populate_obj(home)
        home.userId = current_user.id
        db.session.add(home)
        db.session.commit()
        image = Image()
        form.populate_obj(image)
        image.homeId = home.id
        db.session.add(image)
        db.session.commit()
        print ('>>>>>>>>>>>>',home,',,,,',image)
        return home.to_dict(),Image.to_dict()
    errors = form.errors
    print ('>>>>>>>>>>>>',errors)
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400

@home_routes.route('/<int:id>',methods=["DELETE"])
def deletehome(id):
    print ('>>>>>>>>>>>>',',,,,')
    home = Home.query.get(id)
    image = Image.query.filter(Image.homeId == home.id).all()
    db.session.delete(image)
    db.session.commit()
    db.session.delete(home)
    db.session.commit()
    return




