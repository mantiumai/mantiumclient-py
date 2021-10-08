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
from jsonapi_requests import data
from jsonapi_requests.orm.api_model import JsonApiObjectStub
from jsonapi_requests.orm import ApiModel, AttributeField, repositories


class Organization(ApiModel):

    class Meta:
        type = 'organization'
        api = orm_api
        
    organization_id = AttributeField('organization_id')
    name = AttributeField('name')
    url = AttributeField('url')
    selected = AttributeField('selected')
    license = AttributeField('license')
    license_type_id = AttributeField('license_type_id')
    license_expires = AttributeField('license_expires')
    created_by_name = AttributeField('created_by_name')
    created_by_email = AttributeField('created_by_email')
    created_at = AttributeField('created_at')
    updated_by_name = AttributeField('updated_by_name')
    updated_by_email = AttributeField('updated_by_email')
    updated_at = AttributeField('updated_at')


    @classmethod
    def get_selected(cls):
        selected_endpoint = 'organization/selected'
        response = cls._options.api.endpoint(selected_endpoint).get()
        return cls.from_response_content(response.content)

    @classmethod
    def select_org_by_id(cls, id):
        select_endpoint = f'organization/select/{id}'
        cls._options.api.endpoint(select_endpoint).patch()

    def select_org(self):
        select_endpoint = f'organization/select/{self.id}'
        self._options.api.endpoint(select_endpoint).patch()

    def update(self):
        object = {}
        for k,_ in self.raw_object.attributes.items():
            object[k] = self.raw_object.attributes[k]
        api_response = self.endpoint.patch(json=object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data

    def create(self):
        object = {}
        for k,_ in self.raw_object.attributes.items():
            object[k] = self.raw_object.attributes[k]
        api_response = self.endpoint.patch(json=object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data
    
    def get_users(self):
        org_users_endpoint = f'organization/{self.id}/users'
        response = self._options.api.endpoint(org_users_endpoint).get()
        return OrganizationUser.from_response_content(response.content)
    
    def grant_user_permissions(self, user_id, permission):
        grant_perm_endpoint = f'organization/{self.id}/users/{user_id}'
        self._options.api.endpoint(grant_perm_endpoint).put(data=f'"{permission}"')

    def add_user(self, user_id):
        add_user_endpoint = f'organization/{self.id}/users/{user_id}'
        self._options.api.endpoint(add_user_endpoint).post()


class OrganizationUser(ApiModel):

    class Meta:
        type = 'user'
        path = 'user/id'
        api = orm_api

    user_id = AttributeField('user_id')
    email= AttributeField('email')
    phone_number= AttributeField('phone_number')
    username= AttributeField('username')
    first_name= AttributeField('first_name')
    last_name= AttributeField('last_name')
    picture= AttributeField('picture')
    last_login= AttributeField('last_login')
    logins_count= AttributeField('logins_count')
    blocked= AttributeField('blocked')
    created_at= AttributeField('created_at')
    updated_at= AttributeField('updated_at')
    role= AttributeField('role')
    selected_organization_id= AttributeField('selected_organization_id')
    organization= AttributeField('organization')