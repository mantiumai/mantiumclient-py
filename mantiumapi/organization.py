from .client import orm_api
from jsonapi_requests.orm import ApiModel, AttributeField, RelationField


class Organization(ApiModel):
    class Meta:
        type = 'organization'
        api = orm_api
