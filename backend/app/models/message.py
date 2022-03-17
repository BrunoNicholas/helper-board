from app import db
from sqlalchemy.dialects.postgresql import JSON

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key = True)
    message = db. Column(db.String(100), nullable = False)
    category = db.Column(db.String(100), nullable = True)
    user_from_id = db.Column(db.Integer(), nullable = False)
    user_to_id = db.Column(db.Integer(), nullable = False)
    status = db.Column(db.String(100), nullable = True)
    deleted_at = db.Column(db.Date(), nullable = True)
    created_at = db.Column(db.Date(), nullable = True)
    updated_at = db.Column(db.Date(), nullable = True)
    
    def __init__(self, message, category, user_from_id, user_to_id, status, deleted_at=None, created_at=None, updated_at=None):
        self.message = message
        self.category = category
        self.user_from_id = user_from_id
        self.user_to_id = user_to_id
        self.status = status
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)