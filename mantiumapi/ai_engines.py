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
from jsonapi_requests.orm import ApiModel, AttributeField


class AiEngine(ApiModel):
    """Mantium AiEngine Endpoint

    This module lists AI Engines available via the Mantium API.

    Available methods:
    get_list() : returns a list of all available AI engines
    from_id(id: str) : returns an AI engine from engine id value (accessible in engine_id_values.py)
    from_provider(provider: str) : returns all AI engines available by provider (Cohere, AI21, OpenAI, Mantium) > CASE SENSITIVE

    Example:
        >>> ai_engines = AiEngine.get_list()
    """

    class Meta:
        type = 'ai_engine'
        api = orm_api

    name = AttributeField('name')
    description = AttributeField('description')
    use_cases = AttributeField('use_cases')
    ai_provider = AttributeField('ai_provider')
    cost_ranking = AttributeField('cost_ranking')

    @classmethod
    def get_list(cls, **kwargs):
        engine_path = f'ai/engine/all'
        response = orm_api.endpoint(engine_path).get(**kwargs)
        return cls.from_response_content(response.content)

    @classmethod
    def from_id(cls, id):
        engine_path = f'ai/engine/get/name/{id}'
        response = orm_api.endpoint(engine_path).get()
        return cls.from_response_content(response.content)

    @classmethod
    def from_provider(cls, provider):
        engine_path = f'ai/engine/get/ai/providers/{provider}'
        response = orm_api.endpoint(engine_path).get()
        return cls.from_response_content(response.content)
