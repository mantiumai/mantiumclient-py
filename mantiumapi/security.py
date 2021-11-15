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


class Policy(ApiModel):
    """Mantium Policy Endpoint

    This module reads, manipulates and creates policies

    Examples:
        >>> policies = Policy.get_list()
        >>> policy = Policy.from_id('<uuid>')
    """

    class Meta:
        type = 'security_policy'
        path = 'security/policies'
        api = orm_api

    policy_id = AttributeField('policy_id')
    name = AttributeField('name')
    description = AttributeField('description')
    rules = AttributeField('rules')

    @classmethod
    def from_response_content(cls, jsonapi_response, from_id=False):
        repository = repositories.Repository(cls._options.api.type_registry)
        if isinstance(jsonapi_response.data, (list, tuple)) and from_id is False:
            result = []
            for object in jsonapi_response.data:
                object.id = object.attributes['policy_id']
                assert object.type == cls._options.type
                new = cls(raw_object=object)
                result.append(new)
                repository.add(new)
        elif from_id is True:
            object = jsonapi_response.data[0]
            object.id = object.attributes['policy_id']
            result = cls(raw_object=jsonapi_response.data[0])
            repository.add(result)
        else:
            result = cls(raw_object=jsonapi_response.data)
            repository.add(result)

        repository.update_from_api_response(jsonapi_response)
        return result

    @classmethod
    def from_id(cls, id):
        policy_path = f'security/policy/{id}'
        response = orm_api.endpoint(policy_path).get()
        return cls.from_response_content(response.content, from_id=True)

    def refresh(self):
        policy_path = f'security/policy/{self.id}'
        api_response = orm_api.endpoint(policy_path).get()
        jsonapi_response = api_response.content
        object = jsonapi_response.data[0]
        object.id = object.attributes['policy_id']
        assert object.type == self.type
        assert object.id == self.id
        repository = repositories.Repository(self._options.api.type_registry)
        repository.add(self)
        repository.update_from_api_response(jsonapi_response)


class Rule(ApiModel):
    """Mantium Policy Rule Endpoint

    This module retrieves rules that can be used in Policies

    Examples:
        >>> rules = Rule.get_list()
        >>> rule = Rule.from_id('<uuid>')
    """

    class Meta:
        type = 'security_rule'
        path = 'security/rules'
        api = orm_api

    rule_id = AttributeField('rule_id')
    name = AttributeField('name')
    description = AttributeField('description')
    ai_provider = AttributeField('ai_provider')
    preprocessor = AttributeField('preprocessor')
    postprocessor = AttributeField('postprocessor')
    parameter_template = AttributeField('parameter_template')

    @classmethod
    def from_id(cls, id):
        rule_path = f'security/rule/{id}'
        response = orm_api.endpoint(rule_path).get()
        return cls.from_response_content(response.content)

    def refresh(self):
        rule_path = f'security/rule/{self.id}'
        api_response = orm_api.endpoint(rule_path).get()
        jsonapi_response = api_response.content
        assert jsonapi_response.data.type == self.type
        assert jsonapi_response.data.id == self.id
        repository = repositories.Repository(self._options.api.type_registry)
        repository.add(self)
        repository.update_from_api_response(jsonapi_response)


class Action(ApiModel):
    """Mantium Policy Action Endpoint

    This module reads, manipulates and creates policies

    Examples:
        >>> actions = Action.get_list()
        >>> action = Action.from_id('<uuid>')
    """

    class Meta:
        type = 'action_type'
        path = 'security/action_types'
        api = orm_api

    action_type_id = AttributeField('action_type_id')
    name = AttributeField('name')
    description = AttributeField('description')
    configurable = AttributeField('configurable')
    parameter_template = AttributeField('parameter_template')

    @classmethod
    def from_id(cls, id):
        action_path = f'security/action/{id}'
        response = orm_api.endpoint(action_path).get()
        return cls.from_response_content(response.content)

    def refresh(self):
        action_path = f'security/action/{self.id}'
        api_response = orm_api.endpoint(action_path).get()
        jsonapi_response = api_response.content
        assert jsonapi_response.data.type == self.type
        assert jsonapi_response.data.id == self.id
        repository = repositories.Repository(self._options.api.type_registry)
        repository.add(self)
        repository.update_from_api_response(jsonapi_response)
