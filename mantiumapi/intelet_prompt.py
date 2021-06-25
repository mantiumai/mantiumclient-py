from .client import orm_api
from jsonapi_requests.orm import ApiModel, AttributeField, RelationField


class InteletPrompt(ApiModel):
    class Meta:
        type = 'intelet_prompt'
        api = orm_api
