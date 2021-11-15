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
from jsonapi_requests.orm import ApiModel, AttributeField, RelationField, repositories

from .client import orm_api
from .execute import InteletExecution


class Intelet(ApiModel):
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
        path = 'intelet'
        type = 'intelet'
        api = orm_api

    intelet_id = AttributeField('intelet_id')
    name = AttributeField('name')
    description = AttributeField('description')
    created_at = AttributeField('created_at')
    created_by = AttributeField('created_by')
    created_by_email = AttributeField('created_by_email')
    created_by_name = AttributeField('created_by_name')
    updated_at = AttributeField('updated_at')
    updated_by_email = AttributeField('updated_by_email')
    upcated_by_name = AttributeField('updated_by_name')
    organization_id = AttributeField('organization_id')
    organization_name = AttributeField('organization_name')
    prompts = AttributeField('prompts')
    last_successful_run = AttributeField('last_successful_run')
    deploy_name = AttributeField('deploy_name')
    deploy_description = AttributeField('deploy_description')
    deploy_placeholder = AttributeField('deploy_placeholder')
    deploy_author_name = AttributeField('deploy_author_name')
    deploy_author_contact = AttributeField('deploy_author_contact')
    deploy_type = AttributeField('deploy_type')
    deploy_allow_input = AttributeField('deploy_allow_type')
    deploy_status = AttributeField('deploy_status')

    @classmethod
    def get_result(cls, intelet_execution_id):
        result_path = f'intelet/result/{intelet_execution_id}'
        api_response = orm_api.endpoint(result_path).get()
        return api_response.payload

    def execute(self, input):
        """Executes an Intelet

        Args:
        input: str, The input data for the Intelet

        Returns:
        InteletExecution() object
        """
        intelet_input = f'{{"input":"{input}"}}'
        execute_path = self.endpoint.path + '/execute'
        api_response = self.endpoint.requests.post(api_path=execute_path, data=intelet_input)
        return InteletExecution(intelet_execution_id=api_response.payload['intelet_execution_id'])

    @classmethod
    def from_response_content(cls, jsonapi_response):
        repository = repositories.Repository(cls._options.api.type_registry)
        if isinstance(jsonapi_response.data, (list, tuple)):
            result = []
            for object in jsonapi_response.data:
                object.type = 'intelet'
                object.attributes['prompts'] = _get_prompts(object.attributes['prompts'])
                assert object.type == cls._options.type
                new = cls(raw_object=object)
                result.append(new)
                repository.add(new)
        else:
            assert jsonapi_response.data.type == cls._options.type
            jsonapi_response.data.attributes['prompts'] = _get_prompts(jsonapi_response.data.attributes['prompts'])
            result = cls(raw_object=jsonapi_response.data)
            repository.add(result)
        repository.update_from_api_response(jsonapi_response)
        return result

    def update(self):
        object = {}
        for k, _ in self.raw_object.attributes.items():
            object[k] = self.raw_object.attributes[k]
        api_response = self.endpoint.patch(json=object)
        if api_response.status_code == 200 and api_response.content.data:
            self.refresh()

    def create(self):
        object = {}
        for k, _ in self.raw_object.attributes.items():
            object[k] = self.raw_object.attributes[k]
        api_response = self._options.api.endpoint(self.endpoint_path()).post(json=object)
        if api_response.status_code == 201 and api_response.content.data:
            self.raw_object = api_response.content.data

    def refresh(self):
        api_response = self.endpoint.get()
        jsonapi_response = api_response.content
        jsonapi_response.data.type = 'intelet'
        jsonapi_response.data.id = jsonapi_response.data.attributes['intelet_id']
        jsonapi_response.data.attributes['prompts'] = _get_prompts(jsonapi_response.data.attributes['prompts'])
        assert jsonapi_response.data.type == self.type
        assert jsonapi_response.data.id == self.id
        repository = repositories.Repository(self._options.api.type_registry)
        repository.add(self)
        repository.update_from_api_response(jsonapi_response)


def _get_prompts(prompts):
    try:
        prompts_sort = sorted(prompts, key=lambda i: i['operation_order'])
        prompts = [p['prompt_id'] for p in prompts_sort]
    except:
        prompts = []
    return prompts
