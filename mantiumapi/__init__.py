from .prompt import Prompt
from .tag import Tag
from .intelet import Intelet
from .log import Log
from .intelet_prompt import InteletPrompt
from .prompt_execution import PromptExecution, InteletExecution
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

__all__ = ['Prompt', 'Tag', 'Intelet', 'Log', 'InteletPrompt', 'PromptExecution', 'InteletExecution']


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
