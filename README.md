# Challenge

This is a simple app in Python backend and React JS in the frontend

## Installation

Please follow the installation steps to proceed

### For Backend

Clone the project with a terminal as below

```bash
https://github.com/BrunoNicholas/helper-board.git
```

create a new database with the user name and password to be replace in ```backend\__init__.py``` as ```app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_DB_PATH_AND_USER_CREDENTIALS'```

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
python app.py
```

To run the local server which the frontend will listen to

### For Front end

Please follow the steps to run the frontend instance

## Available end points

| **Method** | **URL** | **Parameters/Body** | **Response** | **Description** |
|------------|-------------|---------------|--------------------|
| GET  | /   |     |    | Entry point |
| GET  | /api/v1/  |    |    | v1 of the API |
| POST | /api/v1/login | email, password | token, message, user | Loggin in Route |
