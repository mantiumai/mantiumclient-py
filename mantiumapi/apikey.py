# -*- coding: utf-8 -*-
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
from jsonapi_requests.orm import ApiModel, AttributeField

from .client import orm_api


class APIKey(ApiModel):
    """ """

    class Meta:
        type = 'api_key'
        path = 'provider/api_keys'
        api = orm_api

    ai_provider = AttributeField('ai_provider')
    api_key = AttributeField('api_key')
    verified = AttributeField('verified')
    created = AttributeField('created')
    updated = AttributeField('updated')

    @classmethod
    def validate(cls, api_key, ai_provider):
        verify_path = f'provider/verify_key/{ai_provider}'
        api_response = orm_api.endpoint(verify_path).post(json={'api_key': api_key})
        if api_response.status == 200:
            return True
        else:
            return False

    def create(self):
        save_path = f'provider/save_key/{self.ai_provider}'
        api_response = orm_api.endpoint(save_path).post(json={'api_key': self.api_key})
        if api_response.status_code == 201:
            self.raw_object = api_response.content.data

    def update(self):
        self.create()

    def save(self):
        self.create()

    def delete(self):
        delete_path = f'provider/delete_key/{self.ai_provider}'
        orm_api.endpoint(delete_path).post(json={'api_key': self.api_key})
