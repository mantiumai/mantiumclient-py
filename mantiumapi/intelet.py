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
from .prompt_execution import InteletExecution
from jsonapi_requests.orm import ApiModel, AttributeField, RelationField, repositories


class Intelet(ApiModel):
    """Mantium Intelet Endpoint

    This module reads, manipulates and creates intelets

    To update the prompts, modify the prompt list on the object by
    inserting the prompt_id. Note that the order of the list
    dictates the order that prompts run, starting at index 0.

    Examples:
        >>> intelets = Intelet.get_list()
        []
        >>> intelet = Intelet.from_id('<uuid>')
        {"data":...}
        >>> intelet.execute('input data')
    """

    class Meta:
        path = 'intelet'
        type = 'intelet_view'
        api = orm_api
        

    intelet_id = AttributeField('intelet_id')
    name = AttributeField('name')
    organization_id = AttributeField('organization_id')
    description = AttributeField('description')
    created_at = AttributeField('created_at')
    updated_at = AttributeField('updated_at')
    created_by = AttributeField('created_by')
    updated_by = AttributeField('updated_by')

    prompts = RelationField('prompts')
    tags = RelationField('tags')

    @classmethod
    def get_result(cls, intelet_execution_id):
        result_path = f'intelet/result/{intelet_execution_id}'
        api_response = orm_api.endpoint(result_path).get()
        return api_response.payload

    def execute(self, input):
        """Executes an intelet using the given input

        Parameters:
            input: string
        """
        intelet_input = f'{{"input":"{input}"}}'
        execute_path = self.endpoint.path + '/execute'
        api_response = self.endpoint.requests.post(api_path=execute_path, data=intelet_input)
        return InteletExecution(intelet_execution_id=api_response.payload['intelet_execution_id'])

    def _get_relation(self, attr):
        r = getattr(self, attr)
        if r is not None and len(r) >= 1:
            relations = [o.id for o in r]
        else:
            relations = []
        return relations

    def update(self):
        modified_object = {'name': self.name, 'description': self.description, 'prompts': self._get_relation('prompts')}
        api_response = self.endpoint.patch(json=modified_object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data

    def create(self):
        modified_object = {'name': self.name, 'description': self.description, 'prompts': self._get_relation('prompts')}
        post_path = f'intelet/'

        api_response = orm_api.endpoint(post_path).post(json=modified_object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data
