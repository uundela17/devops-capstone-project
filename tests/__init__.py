from flask_cors import CORS

def test_cors_security(self):
    """It should return a CORS header"""
    response = self.client.get('/', environ_overrides=HTTPS_ENVIRON)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    # Check for the CORS header
    self.assertEqual(response.headers.get('Access-Control-Allow-Origin'), '*')

CORS(app)
