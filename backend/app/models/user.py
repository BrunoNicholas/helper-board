from tkinter import NO
from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Integer(), nullable=True)
    is_dev = db.Column(db.Integer(), nullable=True)
    is_student = db.Column(db.Integer(), nullable=True)
    status = db.Column(db.String(100), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)
    created_at = db.Column(db.Date(), nullable=True)
    updated_at = db.Column(db.Date(), nullable=True)

    def __init__(self, name, email, password, is_admin, status, is_dev, is_student, deleted_at=None, created_at=None,
                 updated_at=None):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.is_dev = is_dev
        self.is_student = is_student
        self.status = status
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
