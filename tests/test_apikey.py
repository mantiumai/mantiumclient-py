from unittest import mock

from mantiumapi import APIKey

APIKEY = {
    "data": [
        {
            "id": "Cohere",
            "type": "api_key",
            "attributes": {
                "ai_provider": "Cohere",
                "verified": 'true',
                "created": {
                  "timestamp": "2021-10-29T01:29:06.431992+00:00",
                  "user_id": "d0444181-2d60-47dc-a0ea-97604b656a40"
                },
                "updated": 'null'
            },
            "relationships": {}
        }
    ]
}


def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.content = data
            self.json_data = data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'GET' and args[1] == 'https://api.mantiumai.com/v1/provider/api_keys':
        return MockResponse(APIKEY, 200)


@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_apikey(mock_get):
    target = APIKey.get_list()
    assert isinstance(target[0], APIKey)
    assert target[0].id == 'Cohere'
    assert target[0].type == 'api_key'
    assert target[0].attributes['verified'] == 'true'
    assert target[0].attributes['created'] == {
        "timestamp": "2021-10-29T01:29:06.431992+00:00",
        "user_id": "d0444181-2d60-47dc-a0ea-97604b656a40"
    }
    assert target[0].attributes['updated'] == 'null'
