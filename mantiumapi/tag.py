from .client import orm_api
from jsonapi_requests.orm import ApiModel, AttributeField, repositories


class Tag(ApiModel):
    """Tag Endpoint

    This module retrieves and creates Tags

    Examples:
        >>> tags = Tag.get_list()
        []
        >>> tag = Tag.from_id('<uuid>')
        {"data":...}

    """
    class Meta:
        type = 'tag'
        api = orm_api

    tag_id = AttributeField('tag_id')
    name = AttributeField('name')
    organization_id = AttributeField('organization_id')
    description = AttributeField('description')

    def __init__(self, raw_object=None):
        super().__init__(raw_object)
        self.id = self.tag_id

    @classmethod
    def get_list(cls, **kwargs):
        response = orm_api.endpoint(cls.endpoint_path()).get(**kwargs)
        return cls.from_response_content(response.content)

    def refresh(self):
        get_path = f'tag/id/{self.id}'
        api_response = orm_api.endpoint(get_path).get()
        jsonapi_response = api_response.content
        assert jsonapi_response.data.type == self.type
        repository = repositories.Repository(self._options.api.type_registry)
        repository.add(self)
        repository.update_from_api_response(jsonapi_response)

    def update(self):
        modified_object = {'name': self.name, 'description': self.description}
        patch_path = f'tag/'
        api_response = orm_api.endpoint(patch_path).patch(json=modified_object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data

    def create(self):
        modified_object = {'name': self.name, 'description': self.description}
        post_path = f'tag/'
        api_response = orm_api.endpoint(post_path).post(json=modified_object)
        if api_response.status_code == 200 and api_response.content.data:
            self.raw_object = api_response.content.data
