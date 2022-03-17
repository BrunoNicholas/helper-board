from app import db
from sqlalchemy.dialects.postgresql import JSON


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer(), nullable=False)
    accuracy = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(100), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)
    created_at = db.Column(db.Date(), nullable=True)
    updated_at = db.Column(db.Date(), nullable=True)

    def __init__(self, latitude, longitude, user_id, accuracy, status, deleted_at=None, created_at=None,
                 updated_at=None):
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.accuracy = accuracy
        self.status = status
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
