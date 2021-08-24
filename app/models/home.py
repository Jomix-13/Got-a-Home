from .db import db


class Home(db.Model):
    __tablename__ = 'homes'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    stAddress = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String, nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    lotSize = db.Column(db.Integer, nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    bath = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    user = db.relationship("User", back_populates="homes")
    question = db.relationship("Questio", back_populates="homes")
    image = db.relationship("Image", back_populates="homes")

    def to_dict(self):
        return{
            'id': self.id,
            'price': self.price,
            'stAddress': self.stAddress,
            'city': self.city,
            'state': self.state,
            'zipCode': self.zipCode,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'lotSize': self.lotSize,
            'beds': self.beds,
            'bath': self.bath,
            'status': self.status,
            'userId': self.userId,
            'createdAt': self.createdAt
        }