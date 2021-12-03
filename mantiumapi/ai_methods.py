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
from jsonapi_requests.orm import ApiModel, AttributeField, repositories

from .client import orm_api


class AiMethod(ApiModel):
    """Mantium AiMethods Endpoint

    This module lists AI methods available for each provider.
    Example:
        >>> aimethods = AiMethod.get_list(provider="openai")
        provider must be "openai", "cohere", "ai21", or "mantium"
    """

    class Meta:
        type = 'ai_method'
        api = orm_api

    name = AttributeField('name')
    api_name = AttributeField('api_name')
    description = AttributeField('description')
    shareable = AttributeField('shareable')
    endpoint_url = AttributeField('endpoint_url')
    ai_provider = AttributeField('ai_provider')
    ai_engines = AttributeField('ai_engines')

    @classmethod
    def get_list(cls, provider):
        engine_path = f'ai_methods/{provider}'
        response = orm_api.endpoint(engine_path).get()
        return cls.from_response_content(response.content)
