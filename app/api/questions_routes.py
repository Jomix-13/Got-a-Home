from flask import Blueprint, jsonify,request
from app.models import Question,db
from app.forms import QuestionForm
from flask_login import current_user

question_routes = Blueprint('questions', __name__)

@question_routes.route('/')
def allquestions():
    questions = Question.query.order_by(Question.id.desc()).all()
    return {'questions': [question.to_dict() for question in questions]}

@question_routes.route('/add',methods=['POST'])
def addquestion():
    form=QuestionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        question=Question()
        form.populate_obj(question)
        question.userId = current_user.id
        # question.homeId = current_home.id 
        db.session.add(question)
        db.session.commit()
        return question.to_dict()
    errors = form.errors
    print ('>>>>>>>>>>>>',errors)
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400


@question_routes.route('/<int:id>',methods=['DELETE'])
def deletequestion(id):
    question = Question.query.get(id)
    db.session.delete(question)
    db.session.commit()
    print('>>>>>>>>>>>>>>>>',question)
    return "Deleted"



# @home_routes.route('/<int:id>')
# def onehome(id):
#     home = Home.query.get(id)
    
#     return home.to_dict()

#
# @home_routes.route('/<int:id>',methods=["DELETE"])
# def deletehome(id):
#     print ('>>>>>>>>>>>>',',,,,')
#     home = Home.query.get(id)
#     images = Image.query.filter(Image.homeId == home.id).all()
#     for image in images :
#         db.session.delete(image)
#     questions = Question.query.filter(Question.homeId == home.id).all()
#     for question in questions :
#         db.session.delete(question)
#     db.session.delete(home)
#     db.session.commit()
#     return "Deleted"


# @home_routes.route('edit/<int:id>',methods=['PUT'])
# def edithome(id):
#     home = Home.query.get(id)
#     form = HomeForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     if form.validate_on_submit():
#         home.price = form.price.data
#         home.stAddress = form.stAddress.data
#         home.city = form.city.data
#         home.state = form.state.data
#         home.zipCode = form.zipCode.data
#         home.latitude = form.latitude.data
#         home.longitude = form.longitude.data
#         home.lotSize = form.lotSize.data
#         home.beds = form.beds.data
#         home.bath = form.bath.data
#         home.status = form.status.data
#         db.session.commit()

#         image = Image()
#         form.populate_obj(image)
#         db.session.commit()
#         return home.to_dict()
#     errors = form.errors
#     print ('>>>>>>>>>>>>',errors)
#     return jsonify([f'{field.capitalize()}: {error}'
#                 for field in errors
#                 for error in errors[field]]),400






