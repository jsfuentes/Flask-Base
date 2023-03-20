# Python Base

This is a **python 3.10.10 project** with flask base to build off of. It contains the following:

- flask_login setup
- config for different dev and prod configurations
- example get and post routes

## Setup App

1. Setup your db url in `zappa_settings.json` and other config in config.py

```
python -m venv venv
source ./venv/bin/activate
```

## Run App

```
source ./venv/bin/activate
python -m flask --debug run -p 4000
```

_Default of 5000 can cause problems on Mac cuz 5000 is used for control center_
