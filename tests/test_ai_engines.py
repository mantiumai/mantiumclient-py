from unittest import mock

import mantiumapi.ai_engines

AIENGINE = {
    'data': [
        {
            'id': 'b2ffecf7-4fee-42e7-b85d-a5e28d939396',
            'type': 'ai_engine',
            'attributes': {
                'name': 'davinci',
                'description': 'Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and content creative generation, Davinci is going to produce the best results. The trade-off with Davinci is that it costs more to use per API call and other engines are faster.\nAnother area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.',
                'use_cases': 'Complex intent, cause and effect, summarization for audience',
                'ai_provider': 'OpenAI',
                'cost_ranking': '100',
                'ai_engine_id': 'b2ffecf7-4fee-42e7-b85d-a5e28d939396',
                'status': 'READY',
                'base_model_name': '',
                'created_date': 'None',
            },
            'relationships': {},
        }
    ],
    'included': [],
    'meta': {},
    'links': {'total_items': 19, 'current_page': 1},
}

ENGINEBYPROVIDER = {
    'data': [
        {
            'id': '3f7e30f4-46b6-4338-b825-ffb4e87f69c8',
            'type': 'ai_engine',
            'attributes': {
                'name': 'davinci-instruct-beta',
                'description': '',
                'use_cases': '',
                'ai_provider': 'OpenAI',
                'cost_ranking': '0',
                'ai_engine_id': '3f7e30f4-46b6-4338-b825-ffb4e87f69c8',
                'status': 'READY',
                'base_model_name': '',
                'created_date': 'None',
            },
            'relationships': {},
        }
    ],
    'included': [],
    'meta': {},
    'links': {'total_items': 11, 'current_page': 1},
}


def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.content = data
            self.json_data = data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'GET' and args[1] == 'https://api.mantiumai.com/v1/ai/engine/all':
        return MockResponse(AIENGINE, 200)
    elif args[0] == 'GET' and args[1] == 'https://api.mantiumai.com/v1/ai/engine/get/ai/providers/OpenAI':
        return MockResponse(ENGINEBYPROVIDER, 200)
    else:
        return MockResponse('', 404)


@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_ai_engine(mock_get):
    target = mantiumapi.ai_engines.AiEngine.get_list()
    assert isinstance(target[0], mantiumapi.ai_engines.AiEngine)
    assert target[0].name == 'davinci'
    assert (
        target[0].description
        == 'Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction. For applications requiring a lot of understanding of the content, like summarization for a specific audience and content creative generation, Davinci is going to produce the best results. The trade-off with Davinci is that it costs more to use per API call and other engines are faster.\nAnother area where Davinci shines is in understanding the intent of text. Davinci is quite good at solving many kinds of logic problems and explaining the motives of characters. Davinci has been able to solve some of the most challenging AI problems involving cause and effect.'
    )
    assert target[0].use_cases == 'Complex intent, cause and effect, summarization for audience'
    assert target[0].ai_provider == 'OpenAI'
    assert target[0].cost_ranking == '100'


@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_ai_engine_provider(mock_get):
    target = mantiumapi.ai_engines.AiEngine.from_provider('OpenAI')
    assert isinstance(target[0], mantiumapi.ai_engines.AiEngine)
    assert target[0].name == 'davinci-instruct-beta'
    assert target[0].ai_provider == 'OpenAI'
