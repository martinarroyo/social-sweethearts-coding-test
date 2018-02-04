#!/bin/bash
# You need to create the envvars.sh and my.cnf files before running this script, as well as filling the missing fields in deployment/fixtures.json!

if [ ! -d "env" ]; then
virtualenv -p python3.6 env
fi

source env/bin/activate
pip install -r requirements-prod.txt

source envvars.sh 

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata deployment/fixtures.json
