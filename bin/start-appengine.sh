#!/bin/sh
APPSERVER=$APPENGINE/dev_appserver.py
$PYTHON25 $APPSERVER --port=8765 --address=10.1.6.111 app/
