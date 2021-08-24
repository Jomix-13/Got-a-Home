from .db import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    homeId = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    user = db.relationship("User", back_populates="questions")
    home = db.relationship("Home", back_populates="questions")

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'userId': self.userId,
            'homeId': self.homeId,
            'username': self.user.username,
            'createdAt': self.createdAt
        }
