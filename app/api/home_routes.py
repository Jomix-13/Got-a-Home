from flask import Blueprint, jsonify,request
from app.models import Home,db
from app.models import Image,Question
from app.forms import HomeForm
from flask_login import current_user

home_routes = Blueprint('homes', __name__)


@home_routes.route('/')
def allhomes():
    homes = Home.query.order_by(Home.createdAt.desc()).all()
    return {'homes': [home.to_dict() for home in homes]}

@home_routes.route('/splash')
def slashhomes():
    homes20 = Home.query.order_by(Home.createdAt.asc()).limit(20)
    return {'homes': [home.to_dict() for home in homes20]}
@home_routes.route('/buy')
def buyhomes():
    buyhomes = Home.query.filter(Home.status.like("For Sale")).all()
    print('>>>>>>>>>>',buyhomes)
    return {'homes': [home.to_dict() for home in buyhomes]}
@home_routes.route('/rent')
def renthomes():
    renthomes = Home.query.filter(Home.status.like("For Rent")).all()
    return {'homes': [home.to_dict() for home in renthomes]}


@home_routes.route('/<int:id>', methods=['GET'])
def onehome(id):
    home = Home.query.get(id)
    print(home)
    return home.to_dict()

@home_routes.route('/sell',methods=['POST'])
def addhome():
    form = HomeForm()
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
        return home.to_dict(),image.to_dict()
    errors = form.errors
    print ('>>>>>>>>>>>>',errors)
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400

@home_routes.route('/<int:id>',methods=["DELETE"])
def deletehome(id):
    print ('>>>>>>>>>>>>',',,,,')
    home = Home.query.get(id)
    images = Image.query.filter(Image.homeId == home.id).all()
    for image in images :
        db.session.delete(image)
    questions = Question.query.filter(Question.homeId == home.id).all()
    for question in questions :
        db.session.delete(question)
    db.session.delete(home)
    db.session.commit()
    return "Deleted"


@home_routes.route('edit/<int:id>',methods=['PUT'])
def edithome(id):
    home = Home.query.get(id)
    form = HomeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        home.price = form.price.data
        home.stAddress = form.stAddress.data
        home.city = form.city.data
        home.state = form.state.data
        home.zipCode = form.zipCode.data
        home.latitude = form.latitude.data
        home.longitude = form.longitude.data
        home.lotSize = form.lotSize.data
        home.beds = form.beds.data
        home.bath = form.bath.data
        home.status = form.status.data
        db.session.commit()

        image = Image()
        form.populate_obj(image)
        db.session.commit()
        return home.to_dict()
    errors = form.errors
    print ('>>>>>>>>>>>>',errors)
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400






