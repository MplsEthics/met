from webtest import TestApp
from met.app import wsgi_app

app = TestApp(wsgi_app)

def test_index():
    response = app.get('/')
    assert 'Hello world!' in str(response)
