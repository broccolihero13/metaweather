from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_about():
  '''
  Tests that about page returns HTML and is 200 OK
  '''
  response = client.get('/about')
  assert response.status_code == 200
  assert "text/html;" in response.headers['content-type']

def test_404():
  '''
  Tests when a path isn't found and delivers 404 message
  '''
  response = client.get('/not_a_current_path')
  assert response.status_code == 404
  assert response.json() == {"detail": "Not Found"}

