# Challenge

This is a simple app in Python backend and React JS in the frontend

## Installation

Please follow the installation steps to proceed

### For Backend

Clone the project with a terminal as below

```bash
https://github.com/BrunoNicholas/helper-board.git
```

create a new database with the username and password to be replaced in ```backend\__init__.py``` as ```app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_DB_PATH_AND_USER_CREDENTIALS'```

Once you are done, you can then create a new virtual environment as;

```bash
python -m venv nvenv
```

and after activate the virtual environment given your OS, or platform.

Run the commands below ro install the dependencies

```bash
cd backend
pip install -r requirements.txt
```

if this is done, then do the migrations are you see below.

use ```flask db init``` to initialize the connection

use ```flask db migrate``` to create the migrations

use ```flask db upgrade``` to do the actual migrations

Now you can run

```bash
flask run
```

To run the local server which the frontend will listen to

### For Front end

Please follow the steps to run the frontend instance

## Available end points

If we have out base URL as ```http://0.0.0.0:5050```, you can append the endpoints below to archive the goal

| **Method**  | **URL** | **Parameters/Body** | **Response** | **Description** |
| ------------- | --------------- | ----------------- | ---------------------- | --- |
| GET  | /   |     | message  | Entry point |
| GET  | /api/v1/  |    |  message  | v1 of the API, same as /api |
| POST | /api/v1/login | email, password | token, message, user | Authenticating a user to receive a token |
| POST | /api/v1/signup | name, email, password, is_admin, is_dev, is_student, status, active_person   | message, user | Craetion of a new user account |
| GET | /api/v1/user |  | token, message, user, messages, location, chat_status | A sync profile endpoint for the logged in user |
| GET | /api/v1/users |  | message, users, total | A list of all logged in users |
| GET | /api/v1/messages |  | message, messages, total | A list of all logged in user messgaes |
| GET | /api/v1/locations |  | message, locations, total | A list of all logged in user locations details |
| GET | /api/v1/notifications |  | message, notifications, total | A list of all logged in user notifications |
| POST | /api/v1/users |  | message, users, total | Adding a new user (only admin) |
| POST | /api/v1/messages |  | message, messages, total | Adding a new message / sending |
| POST | /api/v1/locations |  | message, locations, total | Adding user location details |
| POST | /api/v1/notifications |  | message, notifications, total | Adding user notification |
| GET | /api/v1/users/\<id> |  | message, users, total | Viewing user details |
| GET | /api/v1/messages/\<id> |  | message, messages, total | viewing message details |
| GET | /api/v1/locations/\<id> |  | message, locations, total | viweing location details |
| GET | /api/v1/notifications/\<id> |  | message, notifications, total | viewing  notification details |
| PUT | /api/v1/users/\<id> |  | message, users, total | updating user details |
| PUT | /api/v1/messages/\<id> |  | message, messages, total | updating message details |
| PUT | /api/v1/locations/\<id> |  | message, locations, total | updating location details |
| PUT | /api/v1/notifications/\<id> |  | message, notifications, total | updating  notification details |
| DELETE | /api/v1/users/\<id> |  | message, users, total | deleting user details |
| DELETE | /api/v1/messages/\<id> |  | message, messages, total | deleting message details |
| DELETE | /api/v1/locations/\<id> |  | message, locations, total | deleting location details |
| DELETE | /api/v1/notifications/\<id> |  | message, notifications, total | deleting  notification details |

## License

MIT
