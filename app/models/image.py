from .db import db


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    homeId = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)

    home = db.relationship("Home", back_populates="images")

    def to_dict(self):
        return {
            'id': self.id,
            'image': self.image,
            'homeId': self.homeId,
        }