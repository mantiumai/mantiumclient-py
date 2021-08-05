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
import json

from jsonapi_requests.orm import ApiModel, AttributeField, repositories, RelationField

from .client import orm_api
from .intelet import Intelet
from .prompt_execution import PromptExecution


class Prompt(ApiModel):
    """Mantium Prompt Endpoint

    This module reads, manipulates and creates prompts

    Examples:
        >>> prompts = Prompt.get_list()
        []
        >>> prompt = Prompt.from_id('<uuid>')
        {"data":...}
        >>> prompt.execute('input data')
    """

    class Meta:
        type = 'prompt'
        api = orm_api

    prompt_id = AttributeField('prompt_id')
    name = AttributeField('name')
    organization_id = AttributeField('organization_id')
    description = AttributeField('description')
    prompt_text = AttributeField('prompt_text')
    status = AttributeField('status')
    ai_provider = AttributeField('ai_provider')
    default_engine = AttributeField('default_engine')
    ai_method = AttributeField('ai_method')
    prompt_parameters = AttributeField('prompt_parameters')
    created_at = AttributeField('created_at')
    last_activity = AttributeField('last_activity')
    
    #intelets = RelationField('intelets')
    tags = RelationField('tags')

    @classmethod
    def get_list(cls, **kwargs):
        response = orm_api.endpoint(cls.endpoint_path()).get(**kwargs)
        return cls.from_response_content(response.content)

    @classmethod
    def get_result(cls, prompt_execution_id):
        result_path = f'prompt/result/{prompt_execution_id}'
        api_response = orm_api.endpoint(result_path).get()
        return api_response.payload

    def execute(self, input):
        """Executes a prompt using the given input

        Parameters:
            input: string
        """
        prompt_input = f'{{"input":"{input}"}}'
        execute_path = f'prompt/{self.id}/execute'
        api_response = orm_api.endpoint(execute_path).post(data=prompt_input)
        return PromptExecution(prompt_execution_id=api_response.payload['prompt_execution_id'])

    def refresh(self):
        get_path = f'prompt/{self.id}'
        api_response = orm_api.endpoint(get_path).get()
        jsonapi_response = api_response.content
        assert jsonapi_response.data.type == self.type
        assert jsonapi_response.data.id == self.id
        repository = repositories.Repository(self._options.api.type_registry)
        repository.add(self)
        repository.update_from_api_response(jsonapi_response)

    def _get_relation(self, attr):
        r = getattr(self, attr)
        if r is not None and len(r) >= 1:
            relations = [o.id for o in r]
        else:
            relations = []
        return relations

    def update(self):
        modified_object = {
            'name': self.name,
            'ai_provider': self.ai_provider,
            'status': self.status,
            'description': self.description,
            'prompt_text': self.prompt_text,
            'ai_method': self.ai_method,
            'default_engine': self.default_engine,
            'prompt_parameters': self.prompt_parameters,
            'intelets': self._get_relation('intelets'),
        }

        patch_path = f'prompt/{self.id}'
        api_response = orm_api.endpoint(patch_path).patch(json=modified_object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data

    def create(self):
        modified_object = {
            'name': self.name,
            'ai_provider': self.ai_provider,
            'status': self.status,
            'description': self.description,
            'prompt_text': self.prompt_text,
            'ai_method': self.ai_method,
            'default_engine': self.default_engine,
            'prompt_parameters': self.prompt_parameters,
            'intelets': self._get_relation('intelets'),
        }
        post_path = f'prompt/'
        api_response = orm_api.endpoint(post_path).post(json=modified_object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data

    def parse(self, parse_type="json", configuration={}):
        post_path = f"prompt/parse/" + parse_type
        self.configuration = configuration
        modified_object = {
            "body": self.import_body
        }
        api_response = orm_api.endpoint(post_path).post(json=modified_object)
        self.raw_object = api_response.content.data
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data
            attributes = self.raw_object.attributes
            self.ai_provider = attributes.get('ai_provider')
            data = attributes['data']
            self.data = data
            self.name = data.get('name', configuration.get('name'))
            self.description = data.get('description', configuration.get('description'))
            self.status = data.get('status', configuration.get('status'))
            self.ai_method = data.get('ai_method', configuration.get('ai_method'))
            default_engine = None
            for key in ['default_engine', 'endpoint', 'engine']:
                if key in data and data.get(key):
                    default_engine = data.get(key)
                elif key in configuration and configuration.get(key):
                    default_engine = configuration.get(key)
                if default_engine:
                    self.default_engine = default_engine
            self.prompt_text = data.get('prompt')
            self.prompt_parameters = {
                'basic_settings': configuration.get('basic_settings', data.get('basic_settings')),
                'advanced_settings': configuration.get('advanced_settings', data.get('advanced_settings')),
            }
