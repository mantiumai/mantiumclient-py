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
from posixpath import basename
import requests
import os
from .client import orm_api
from jsonapi_requests.orm import ApiModel, AttributeField


class OpenAIFiles(ApiModel):
    class Meta:
        type = 'openai_file'
        path = 'files/openai_files'
        api = orm_api

    organization = AttributeField('organization')
    files = AttributeField('files')

    @classmethod
    def from_id():
        pass

    @classmethod
    def get_list(cls, **kwargs):
        if 'params' in kwargs:
            if not 'file_type' in kwargs['params']:
                kwargs['params']['file_type'] = 'FILES_ONLY'
        else:
            kwargs['params'] = {'file_type': 'FILES_ONLY'}
        response = cls._options.api.endpoint(cls.endpoint_path()).get(**kwargs)
        return cls.from_response_content(response.content)

    @classmethod
    def from_response_content(cls, jsonapi_response):
        result = []
        try:
            for object in jsonapi_response.data.attributes['files']:
                new = OpenAIFile(**object)
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
            raise ValueError(
                f"Purpose '{purpose}' must be 'classifcations', 'search', or 'answers'"
            )

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
                raise Exception(
                    'Unexpected issue while uploading file. '
                    'Status Code: ' + str(response.status_code)
                )

    @classmethod
    def delete(cls, id):
        delete_endpoint = f'files/openai_files/{id}'
        orm_api.endpoint(delete_endpoint).delete()


class OpenAIFile:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def delete(self):
        OpenAIFiles.delete(self.id)


class FinetuneFile:
    pass
