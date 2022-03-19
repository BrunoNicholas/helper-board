from ..models.notification import Notification


def index(user_id=None, user_type=None):
    notifications = Notification.query.all()
    output = []

    if user_id and user_type is 'developer' or user_id and user_type is 'student':
        for message in notifications:
            if message.user_from_id is user_id or message.user_to_id is user_id:
                output.append({
                    'id': message.id,
                    'message': message.notification,
                    'category': message.cetegory,
                    'from': message.user_from_id,
                    'to': message.user_to_id,
                    'status': message.status,
                    'deleted': True if message.deleted_at else False,
                    'created': message.created_at,
                    'last_update': message.updated_at,
                })

    else:
        for message in notifications:
            output.append({
                'id': message.id,
                'message': message.notification,
                'category': message.cetegory,
                'from': message.user_from_id,
                'to': message.user_to_id,
                'status': message.status,
                'deleted': True if message.deleted_at else False,
                'created': message.created_at,
                'last_update': message.updated_at,
            })

    return output


def store():
    pass


def show():
    pass


def update():
    pass


def destroy():
    pass
