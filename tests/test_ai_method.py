import unittest
from unittest import mock

from mantiumapi import AiMethod

AI_METHODS = {
    'data': [
        {
            'id': 'answers',
            'type': 'ai_method',
            'attributes': {
                'type': 'ai_method',
                'name': 'answers',
                'api_name': 'answers',
                'description': 'Returns answers',
                'shareable': 'true',
                'endpoint_url': 'https://api.openai.com/v1/answers',
                'ai_provider': {'name': 'OpenAI', 'description': 'OpenAI -- https://openai.org'},
                'ai_engines': [
                    {
                        'name': 'cursing-filter-v6',
                        'status': 'READY',
                        'use_cases': '',
                        'description': '',
                        'ai_engine_id': '78399e12-fa98-4dd5-8800-2fc41b28033f',
                        'cost_ranking': 0,
                    },
                    {
                        'name': 'davinci',
                        'status': 'READY',
                        'use_cases': 'Complex intent, cause and effect, summarization for audience',
                        'description': 'Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and content creative generation, Davinci is going to produce the best results. The trade-off with Davinci is that it costs more to use per API call and other engines are faster.\nAnother area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.',
                        'ai_engine_id': 'b2ffecf7-4fee-42e7-b85d-a5e28d939396',
                        'cost_ranking': 100,
                    },
                ],
            },
            'relationships': {},
        }
    ],
    'included': [],
    'meta': {},
    'links': {'total_items': 4, 'current_page': 1},
}


def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.content = data
            self.json_data = data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'GET' and args[1] == 'https://api.mantiumai.com/v1/ai_methods/openai':
        return MockResponse(AI_METHODS, 200)


@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_ai_method(mock_get):
    target = AiMethod.get_list(provider='openai')
    assert isinstance(target[0], AiMethod)
    assert target[0].type == 'ai_method'
    assert target[0].name == 'answers'
    assert target[0].api_name == 'answers'
    assert target[0].description == 'Returns answers'
    assert target[0].shareable == 'true'
    assert target[0].endpoint_url == 'https://api.openai.com/v1/answers'
    assert target[0].ai_provider == {
        'name': 'OpenAI', 'description': 'OpenAI -- https://openai.org'
    }
    assert target[0].ai_engines[0] == {
        'name': 'cursing-filter-v6',
        'status': 'READY',
                'use_cases': '',
                'description': '',
                'ai_engine_id': '78399e12-fa98-4dd5-8800-2fc41b28033f',
                'cost_ranking': 0
    }
