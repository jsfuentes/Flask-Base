# Python SIMPLE Base
This is a python flask base to build off of. It contains the following:
- factory method for different dev/prod configurations
- example get 
- file structure
- pipenv runtime setup
- automatically reload on changes

## Setup App
1. `pip install pipenv`
2. In the main directory, `pipenv install`, this handles your virtual environment using the Pipfile much like npm

## Run App
1. `pipenv shell` enters the virtual environment
2. `flask run`, runs app.py with .env variables

*Can also not shell and prefix any command with `pipenv run` i.e `pipenv run flask run``*

