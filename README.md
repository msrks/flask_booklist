## Booklist Management App

[![CircleCI](https://circleci.com/gh/msrks/circle_ci_test.svg?style=svg)](https://circleci.com/gh/msrks/circle_ci_test)

### Usage

#### 1. configure environment

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

#### 2. create new database (first time only)

```
(venv) $ python
>>> from app import db
>>> db.create_all()
```

#### 3. run app & open http://localhost:5000

```
(venv) $ export FLASK_APP=booklist.py
(venv) $ flask run
```

#### (if database changed) migrate database

```
(venv) $ flask db init #(first time only)
(venv) $ db migrate -m "<commit_message>"
(venv) $ flask db upgrade
```

### How to Contribute

please read [CONTRIBUTING.md](CONTRIBUTING.md) 