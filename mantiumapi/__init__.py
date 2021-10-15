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
from .prompt import Prompt
from .tag import Tag
from .intelet import Intelet
from .log import Log
from .execute import PromptExecution, InteletExecution
from .ai_engines import AiEngine
from .ai_methods import AiMethods
from .license import License
from .organization import Organization
from .files import Files
from .apikey import APIKey
from .security import Policy, Rule, Action
from jsonapi_requests.data import (
    Record,
    JsonApiObject,
    SchemaAlternativeWrapper,
    make_collection,
    List,
    Scalar,
    Dictionary,
)
from jsonapi_requests import data

__all__ = [
    'Prompt',
    'Tag', 
    'Intelet', 
    'Log', 
    'PromptExecution', 
    'InteletExecution', 
    'AiEngine',
    'AiMethods',
    'License',
    'Organization',
    'Files',
    'APIKey',
    'Policy',
    'Rule',
    'Action'
    ]


class MJsonApiResponse(Record):
    schema = {
        'data': SchemaAlternativeWrapper(JsonApiObject, make_collection(List, JsonApiObject, allow_empty_data=True)),
        'errors': List,
        'meta': Scalar,
        'jsonapi': Scalar,
        'links': Dictionary,
        'included': make_collection(List, JsonApiObject),
    }

    # noinspection PyMissingConstructor
    def __init__(self, *, data=None, errors=None, meta=None, jsonapi=None, links=None, included=None):
        if data is None:
            self.data = JsonApiObject()
        else:
            self.data = data
        self.errors = errors or List()
        self.meta = meta
        self.jsonapi = jsonapi
        self.links = links or Dictionary()
        self.included = List()


data.JsonApiResponse = MJsonApiResponse
