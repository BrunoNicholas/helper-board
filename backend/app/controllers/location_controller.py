from ..models.location import Location


def index(user=None):
    if user:
        pass

    locations = Location.query.all()
    output = []

    for location in locations:
        output.append({
            'id': location.id,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'user': location.user_from_id,
            'status': location.status,
            'deleted': True if location.deleted_at else False,
            'created': location.created_at,
            'last_update': location.updated_at,
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
