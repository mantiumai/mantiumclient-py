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
import os
from posixpath import basename

import requests
from jsonapi_requests.orm import ApiModel, AttributeField

from .client import orm_api


class Files(ApiModel):
    class Meta:
        type = 'openai_file'
        path = 'files'
        api = orm_api

    organization = AttributeField('organization')
    files = AttributeField('files')

    @classmethod
    def from_id():
        pass

    @classmethod
    def from_response_content(cls, jsonapi_response):
        result = []
        # maybe check if files > 1, if so then just return 1 object
        try:
            for object in jsonapi_response.data.attributes['files']:
                new = File(**object)
                result.append(new)
        except KeyError:
            pass
        return result

    @classmethod
    def upload(cls, file, purpose, upload_source):
        signature_endpoint = 'files/aws/signature'
        purposes = ['classifications', 'search', 'answers']
        filename = os.path.basename(file)

        if purpose not in purposes:
            raise ValueError(f"Purpose '{purpose}' must be 'classifcations', 'search', or 'answers'")

        response = cls._options.api.endpoint(signature_endpoint).post(
            json={
                'key': filename,
                'purpose': purpose,
                'upload_source': upload_source,
            }
        )

        url = response.data.attributes['url']
        with open(file, 'rb') as data:
            response = requests.put(url, data=data)
            if response.status_code != 200:
                raise Exception('Unexpected issue while uploading file. ' 'Status Code: ' + str(response.status_code))

    @classmethod
    def delete(cls, id):
        delete_endpoint = f'files/{id}'
        orm_api.endpoint(delete_endpoint).delete()


class File:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def delete(self):
        Files.delete(self.id)
