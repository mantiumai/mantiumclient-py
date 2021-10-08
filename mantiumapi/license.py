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
from jsonapi_requests.orm import ApiModel, AttributeField
from .client import orm_api


class License(ApiModel):
    """Mantium License Endpoint

    This module lists available Mantium licences

    Examples:
        >>> licences = License.get_list()
        []
        >>> licence = License.from_id('<uuid>')
        {"data":...}

    """

    class Meta:
        type = 'license'
        api = orm_api
        

    name = AttributeField('name')
    description = AttributeField('description')
    log_retention = AttributeField('log_retention')
    max_prompts = AttributeField('max_prompts')
    cost_per = AttributeField('cost_per')
    billing_cycle = AttributeField('billing_cycle')
    data_serialization = AttributeField('data_serialization')
    human_in_the_loop = AttributeField('human_in_the_loop')
    m_log_events = AttributeField('m_log_events')
    secure_vault = AttributeField('secure_vault')
    security_features = AttributeField('security_features')
    sensitive_data_detection = AttributeField('sensitive_data_detection')