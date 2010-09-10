GAEBASE="/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine"

PYTHONPATH=$PYTHONPATH:$GAEBASE/
PYTHONPATH=$PYTHONPATH:$GAEBASE/lib/
PYTHONPATH=$PYTHONPATH:$GAEBASE/lib/django/
PYTHONPATH=$PYTHONPATH:$GAEBASE/lib/ipaddr/
PYTHONPATH=$PYTHONPATH:$GAEBASE/lib/webob/
PYTHONPATH=$PYTHONPATH:/Users/johntrammell/work/github/met/mpls-ethics

export PYTHONPATH
