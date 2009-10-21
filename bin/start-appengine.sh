#!/bin/sh

APPSERVER=$APPENGINE/dev_appserver.py

if [ "$(hostname)" == 'voh' ]; then
    ADDRESS=127.0.0.1
else
    echo $(hostname)
    ADDRESS=10.1.6.111
fi

$PYTHON25 $APPSERVER --port=8765 --address=$ADDRESS mpls-ethics/
