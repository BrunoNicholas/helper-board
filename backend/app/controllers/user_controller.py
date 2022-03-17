from ..models.user import User


class UserController:
    user = None

    def __init__(self, user=None):
        self.user = user

    def index(self):
        users = User.query.all()

        # converting the query objects to list of jsons
        output = []

        for user in users:
            output.append({
                'public_id': user.public_id,
                'name': user.name,
                'email': user.email,
                'is_dev': user.is_dev
            })

        return users
