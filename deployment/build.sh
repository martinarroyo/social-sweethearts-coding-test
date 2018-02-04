#!/bin/bash
# You need to create the envvars.sh file before running this script!

if [ ! -d "env" ]; then
virtualenv -p python3.6 env
fi

source env/bin/activate
pip install -r requirements.txt

source envvars.sh 

python manage.py migrate
python manage.py collectstatic --yes

