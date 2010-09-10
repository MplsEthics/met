from webtest import TestApp
from pprint import pprint; import sys; pprint(sys.path)

from met.app import wsgi_app

app = TestApp(wsgi_app)

def test_index():
    response = app.get('/')
    assert 'Hello world!' in str(response)
