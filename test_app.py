from app import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello Everyone! from Devops!!!!'
    assert response.status_code == 200
