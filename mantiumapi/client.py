import os
import requests
import time
import jwt
from jsonapi_requests.orm import OrmApi
from requests.auth import AuthBase

ROOT_URL = os.getenv('ROOT_URL', 'https://api.mantiumai.com')

class BearerAuth(AuthBase):
    auth_url = ROOT_URL + '/auth/login/access/token'

    def __init__(self):
        self.token = os.getenv('MANTIUM_TOKEN')
        self.user = os.getenv('MANTIUM_USER')
        self.password = os.getenv('MANTIUM_PASSWORD')

        if self.token is None:
            if not self.user and self.password:
                raise ValueError('Make sure both MANTIUM_USER and MANTIUM_PASS or alternatively just '
                                 'MANTIUM_TOKEN are set in your environment variables.')

    def __call__(self, r):
        self.token = self.get_token()
        r.headers['authorization'] = 'Bearer ' + self.token
        return r

    def check_expire_claim(self):
        if self.token is None:
            return True
        try:
            payload = jwt.decode(self.token, options={'verify_signature': False})
        except:
            return True
        try:
            exp = payload['exp']
        except:
            return True

        now = time.time()
        if now - exp > 10:
            return True
        else:
            return False

    def get_token(self):
        if not self.check_expire_claim():
            return self.token
        else:
            r = requests.post(self.auth_url, json={'username': self.user, 'password': self.password})
        if r.status_code == 403:
            raise ValueError('Username or password incorrect, or token invalid')
        elif r.status_code == 422:
            raise ValueError('Credentials were unprocessable by the API.')
        elif r.status_code != 200:
            raise Exception('Unexpected issue while attempting to authenticate to the Mantium API. '
                            'Status Code: ' + str(r.status_code)) 
        elif r.status_code == 200:
            self.token = r.json()['data']['attributes']['bearer_id']
            return self.token


orm_api = OrmApi.config(
    {
        'API_ROOT': ROOT_URL + '/v1', 
        'AUTH': BearerAuth(), 
        'VALIDATE_SSL': True, 
        'TIMEOUT': 5, 
        'APPEND_SLASH': False
    }
)
