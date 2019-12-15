# CI/CD Sample App


The purpose of this app is to practice CI/CD. 

This app is a simple Flask project that serves basic html and contains one test file.

Use the following commands to run the project:

### Setup Virtual Environment

`python3 -m pip intsall virtualenv`

##### In the root directory of the app

`python3 -m virtualenv env`

### Activate the Virtual Enviornment

`. env/bin/activate`

### Install dependencies
`pip install -r requirements.txt`

### Run Server

`export FLASK_APP=app`

`export FLASK_ENV=development`

`flask run`

got to `localhost:5000/test`

### Run Unit tests
Configure VS Code extsion to work with PyTest