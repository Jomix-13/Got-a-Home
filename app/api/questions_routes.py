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
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400


@question_routes.route('/<int:id>',methods=['DELETE'])
def deletequestion(id):
    question = Question.query.get(id)
    db.session.delete(question)
    db.session.commit()
    return "Deleted"

@question_routes.route('edit/<int:id>',methods=['PUT'])
def editquestion(id):
    question = Question.query.get(id)
    form=QuestionForm()
    print(question,form)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        question.question = form.question.data
        db.session.commit()
        return question.to_dict()
    errors = form.errors
    return jsonify([f'{field.capitalize()}: {error}'
                for field in errors
                for error in errors[field]]),400






