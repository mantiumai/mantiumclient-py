#  Copyright (c) 2021 Mantium, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# Please refer to our terms for more information:
#     https://mantiumai.com/terms-of-use/
#
import os
import unittest
from unittest import mock
from datetime import datetime, timedelta

import base64
import json
import time
import mantiumapi.client
from pytest import raises

decoded_jwt = {
    'given_name': 'Test',
    'family_name': 'User',
    'nickname':
    'rick', 
    'name': 'Test User', 
    'picture': 'https://s.gravatar.com/avatar/31201667409165d2ebb4472d7e01ccd2?s=480&r=pg',
    'updated_at': '2021-03-24T18:11:02.938Z',
    'email': 'test@fakesite.com', 
    'email_verified': True,
    'iss': 'https://fakesite.com/', 
    'sub': '23r5tewgsdsdkjg', 
    'aud': 'ABCDEFG', 
    'iat': time.time(), 
    'exp': time.time() + 60*60
 }


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({
                            "data": {
                                "id": "f79fbc7f-bbd3-4c4a-852a-c2cecbc5aac6",
                                "attributes": {
                                "bearer_id": make_jwt(decoded_jwt),
                                "expires_on": time.time() + 60*60,
                                "token_type": "Bearer"
                                },
                                "relationships": {}
                            },
                            "included": None,
                            "meta": None,
                            "links": None
                            }, 200)

    return MockResponse({"detail":"invalid_request"}, 400)

def make_jwt(decoded_jwt:str, expires_time=time.time() + 60*60, encoding='utf-8'):
    decoded_jwt['exp'] = expires_time
    return "eyJhbGciOiJOb25lIiwidHlwIjoiSldUIiwia2lkIjoibDdhNkVkcVExRmJ6dm9ZOTUwWEsyIn0." + base64.urlsafe_b64encode(
        json.dumps(decoded_jwt).encode(encoding)
    ).decode(encoding).rstrip('=') + "."
   

@mock.patch.dict(
    os.environ, {
            'MANTIUM_USER': "user_id", 
            'MANTIUM_PASSWORD': 'password'
        }
    )
def test_bearerauth_defaults_with_username_pass():
    target = mantiumapi.client.BearerAuth()
    assert target.user is not None
    assert target.user == 'user_id'
    assert target.password is not None
    assert target.password == 'password'
    assert target.token is None
    assert target.auth_url == 'https://api.mantiumai.com/auth/login/access/token'


@mock.patch('requests.post', side_effect=mocked_requests_post)
@mock.patch.dict(
    os.environ, {
            'MANTIUM_USER': "user_id",
            'MANTIUM_PASSWORD': 'password'
        }
    )
def test_bearerauth_get_token(mock_post):
    target = mantiumapi.client.BearerAuth().get_token()
    assert target == make_jwt(decoded_jwt)


@mock.patch('requests.post', side_effect=mocked_requests_post)
@mock.patch.dict(
    os.environ, {
            'MANTIUM_USER': '',
            'MANTIUM_PASSWORD': '',
            'MANTIUM_TOKEN': ''
        }
    )
def test_bearerauth_no_token_username_or_pass(mock_post):
    with raises(ValueError):
        mantiumapi.client.BearerAuth().get_token()


@mock.patch.dict(
    os.environ, {
            'MANTIUM_USER': '',
            'MANTIUM_PASSWORD': '',
            'MANTIUM_TOKEN': make_jwt(decoded_jwt, expires_time=time.time() - 60*60)
        }
    )
def test_bearerauth_check_expire_claim_expired_token():
    client = mantiumapi.client.BearerAuth()
    target = client.check_expire_claim()
    assert target is True


@mock.patch.dict(
    os.environ, {
            "MANTIUM_USER": '',
            'MANTIUM_PASSWORD': '',
            'MANTIUM_TOKEN': make_jwt(decoded_jwt, expires_time=time.time() + 60*60)
        }
    )
def test_bearerauth_check_expire_claim_unexpired_token():
    client = mantiumapi.client.BearerAuth()
    target = client.check_expire_claim()
    assert target is False

