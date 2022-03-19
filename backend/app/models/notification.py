from app import db


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    notification = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    user_from_id = db.Column(db.BIGINT(), nullable=False)
    user_to_id = db.Column(db.BIGINT(), nullable=False)
    status = db.Column(db.String(100), nullable=True)
    deleted_at = db.Column(db.TIMESTAMP(), nullable=True)
    created_at = db.Column(db.TIMESTAMP(), nullable=True)
    updated_at = db.Column(db.TIMESTAMP(), nullable=True)

    def __init__(self, notification, category, user_from_id, user_to_id, status, deleted_at=None, created_at=None,
                 updated_at=None):
        self.notification = notification
        self.category = category
        self.user_from_id = user_from_id
        self.user_to_id = user_to_id
        self.status = status
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
