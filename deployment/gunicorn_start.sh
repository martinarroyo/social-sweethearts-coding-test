#!/bin/bash
BASE_DIR='/home/martin/social-sweethearts-coding-test/social-sweethearts-coding-test'

NAME="social_sweethearts_coding_test"
DJANGODIR=$BASE_DIR
SOCKFILE=$BASE_DIR/run/gunicorn.sock
USER=martin
GROUP=martin
NUM_WORKERS=3

source $BASE_DIR/envvars.sh

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
source $BASE_DIR/env/bin/activate

export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec $BASE_DIR/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
