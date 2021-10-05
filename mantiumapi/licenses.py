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