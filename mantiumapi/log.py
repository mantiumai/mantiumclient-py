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
from jsonapi_requests.orm import ApiModel, AttributeField, RelationField


class Log(ApiModel):
    class Meta:
        type = 'log'
        api = orm_api

    log_id = AttributeField('log_id')
    organization_id = AttributeField('organization_id')
    event_timesteamp = AttributeField('event_timestamp')
    log_type = AttributeField('log_type')
    log_payload = AttributeField('log_payload')
    log_level = AttributeField('log_level')
