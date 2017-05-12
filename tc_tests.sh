#!/usr/bin/env bash

VENV=./venv

export ADRAFT_DATABASE_NAME='adraft'
export ADRAFT_DATABASE_USER='adraft'
export ADRAFT_DATABASE_PASSWORD='123456'
export ADRAFT_DATABASE_HOST='127.0.0.1'
export ADRAFT_DATABASE_PORT='5432'
export ADRAFT_SECRET_KEY='(l3-jtu8c_5$=sgh+9zme1^t-^mbq6nsi+s4x7r6esvxhyeo3v'

virtualenv --python=python3.5 --quiet --no-site-packages $VENV
chmod +x $VENV/bin/activate
. $VENV/bin/activate

pip install -r requirements_test.txt

py.test
