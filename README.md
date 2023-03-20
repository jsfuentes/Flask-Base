# Python Base

This is a python 3.10.10 project with flask base to build off of. It contains the following:

- flask_login setup
- config for different dev and prod configurations
- example get and post routes

## Setup App

1. Setup your db url in `zappa_settings.json`

```
python -m venv venv
source ./venv/bin/activate
```

## Run App

```
source ./venv/bin/activate
flask run --debug
```
