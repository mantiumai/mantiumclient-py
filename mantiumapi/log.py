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
