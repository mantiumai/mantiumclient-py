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
from .client import orm_api
from jsonapi_requests.orm import ApiModel, AttributeField, repositories


class AiMethods(ApiModel):
    """Mantium Intelet Endpoint

    This module reads, manipulates and creates intelets

    To update the prompts, modify the prompt list on the object by
    inserting the prompt_id. Note that the order of the list
    dictates the order that prompts run, starting at index 0.

    Examples:
        >>> intelets = Intelet.get_list()
        >>> intelet = Intelet.from_id('<uuid>')
        >>> intelet.execute('input data')
    """

    class Meta:
        type = 'ai_methods'
        api = orm_api

    name = AttributeField('name')
    api_name = AttributeField('use_cases')
    description = AttributeField('description')
    shareable = AttributeField('sharable')
    ai_provider = AttributeField('ai_provider')
    ai_engines = AttributeField('ai_engines')

    @classmethod
    def get_list(cls, provider):
        engine_path = f'ai_methods/{provider}'
        response = orm_api.endpoint(engine_path).get()
        return cls.from_response_content(response.content)

    @classmethod
    def from_response_content(cls, jsonapi_response):
        repository = repositories.Repository(cls._options.api.type_registry)
        if isinstance(jsonapi_response.data, (list, tuple)):
            result = []
            for object in jsonapi_response.data:
                object.type = 'ai_methods'
                object.id = f'{object.attributes["name"]}-{object.attributes["ai_provider"]["name"]}'
                new = cls(raw_object=object)
                result.append(new)
                repository.add(new)
        else:
            jsonapi_response.data.id = (
                f'{jsonapi_response.data.attributes["name"]}-{jsonapi_response.data.attributes["ai_provider"]["name"]}'
            )
            result = cls(raw_object=jsonapi_response.data)
            repository.add(result)
        repository.update_from_api_response(jsonapi_response)
        return result
