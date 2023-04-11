# Python Base

This is a **python 3.9.16 project** with flask base to build off of. It contains the following:

- flask_login setup
- config for different dev and prod configurations
- example get and post routes
- postgres db setup with flask-sqlalchemy and flask-migrate
- basic user model

## Setup App

Setup local virtual environment and install prereqs

```
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Initial DB and Deployment Setup

Globally required only once

```
zappa init
```

Setup your db url in `zappa_settings.json` by adding `environment_variables` object under the production object with key `DATABASE_URL`.
Also setup other configs in config.py

Then run this to create the db tables

```
flask db init
flask db migrate -m "init"
flask db upgrade
```

And finally deploy to zappa with

```
zappa deploy production
```

## Run App

```
source ./venv/bin/activate
python -m flask --debug run -p 4000
```

_Default of 5000 can cause problems on Mac cuz 5000 is used for control center_

## Migrations

Migrations are handle by flask-migrate/alembic

To autogenerate migration files, in base folder

```
flask db migrate -m "Initial migration."
```

```
flask db upgrade
```

## Update Deployment

Update with

```
zappa update production
```

Tail logs with

```
zappa tail production
```
