#!/bin/bash
BASE_DIR=$PWD

NAME="social_sweethearts_coding_test"
DJANGODIR=$BASE_DIR
SOCKFILE=$BASE_DIR/run/gunicorn.sock
USER=martin
GROUP=martin
NUM_WORKERS=3

source envvars.sh

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
source ./env/bin/activate

export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ./env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
