#!/bin/sh

APPSERVER=$APPENGINE/dev_appserver.py
ADDRESS=127.0.0.1

echo $PYTHON25 $APPSERVER --port=8765 --address=$ADDRESS mpls-ethics/

$PYTHON25 $APPSERVER --port=8765 --address=$ADDRESS mpls-ethics/
