from webtest import TestApp
from met.app import wsgi_app

app = TestApp(wsgi_app)

def test_index():
    #import met; met.debug()
    response = app.get('/')
    assert('302' in response.status)
