from ..models.user import User


def index():
    users = User.query.all()
    output = []

    for user in users:
        output.append({
            'id': user.id,
            'public_id': user.public_id,
            'name': user.name,
            'email': user.email,
            'admin': True if user.is_admin else False,
            'developer': True if user.is_dev else False,
            'student': True if user.is_student else False,
            'status': user.status,
            'deleted': True if user.deleted_at else False,
            'created': user.created_at,
            'last_update': user.updated_at,
            'in_chat': True if user.active_person else False
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


class UserController:
    user = None

    def __init__(self, user=None):
        self.user = user
