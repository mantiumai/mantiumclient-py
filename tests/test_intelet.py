import unittest
from unittest import mock

import mantiumapi.execute
import mantiumapi.intelet

INTELET = {
    'data': {
        'id': '7a2ccb00-85c0-4d70-bf98-779524a73e0f',
        'type': 'intelet_view',
        'attributes': {
            'intelet_id': '7a2ccb00-85c0-4d70-bf98-779524a73e0f',
            'name': 'Test Intelet',
            'description': 'Test Intelet Description',
            'created_at': '2021-01-01T00:00:00.000000+00:00',
            'created_by': '31418670-2905-4875-ae36-02908bafaa52',
            'created_by_email': 'example@example.com',
            'created_by_name': ' ',
            'updated_at': '2021-01-02T00:00:00.000000+00:00',
            'updated_by_email': 'example@example.com',
            'updated_by_name': ' ',
            'organization_id': '55ef3083-6bb5-4794-bb5b-706f20597084',
            'organization_name': ' ',
            'tags': 'null',
            'prompts': [
                {
                    'prompt_id': '6a2ccb00-85c0-33dd-bf98-779524a73e0f',
                    'prompt_name': 'Test prompt 1',
                    'operation_order': 1,
                },
                {
                    'prompt_id': '5a2ccb00-85c0-33dd-bf98-779524a73e0f',
                    'prompt_name': 'Test prompt 2',
                    'operation_order': 2,
                },
                {
                    'prompt_id': '4a2ccb00-85c0-33dd-bf98-779524a73e0f',
                    'prompt_name': 'Test prompt 3',
                    'operation_order': 3,
                },
            ],
        },
        'relationships': {},
    },
    'included': [],
    'meta': {},
    'links': {},
}

INTELET_EXECUTE = {
    'success': 'true',
    'intelet_id': '7a2ccb00-85c0-4d70-bf98-779524a73e0f',
    'input': 'test input',
    'status': 'QUEUED',
    'intelet_execution_id': 'c638ce5f-67e2-4d99-8d28-b1535f41e55d',
    'error': '',
}

INTELET_EXECUTE_RESULT = {
    'intelet_execution_id': 'c638ce5f-67e2-4d99-8d28-b1535f41e55d',
    'intelet_id': '7a2ccb00-85c0-4d70-bf98-779524a73e0f',
    'status': 'QUEUED',
    'input': 'test input',
    'output': 'test output',
    'error': 'error',
    'reason': 'reason',
    'results': [],
    'pending_prompts': [
        '5a2ccb00-85c0-33dd-bf98-779524a73e0f',
        '4b823574-f963-45d4-9e17-1f26bdd612e0',
    ],
    'executed_prompts': [
        {
            'status': 'COMPLETED',
            'prompt_execution_id': '0edcef2e-3c6d-407c-afe7-f73fe78d1972',
            'prompt_id': '6a2ccb00-85c0-33dd-bf98-779524a73e0f',
            'input': 'test input',
            'output': '{}',
            'reason': 'reason',
            'error': 'error',
            'hitl_info': 'null',
        }
    ],
}


def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.content = data
            self.json_data = data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'GET' and args[1] == 'https://api.mantiumai.com/v1/intelet/7a2ccb00-85c0-4d70-bf98-779524a73e0f':
        return MockResponse(INTELET, 200)
    elif (
        args[0] == 'GET'
        and args[1] == 'https://api.mantiumai.com/v1/intelet/result/c638ce5f-67e2-4d99-8d28-b1535f41e55d'
    ):
        return MockResponse(INTELET_EXECUTE_RESULT, 200)
    elif (
        args[0] == 'POST'
        and args[1] == 'https://api.mantiumai.com/v1/intelet/7a2ccb00-85c0-4d70-bf98-779524a73e0f/execute'
    ):
        return MockResponse(INTELET_EXECUTE, 200)
    else:
        return MockResponse('', 404)


@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_intelet(mock_get):
    target = mantiumapi.intelet.Intelet.from_id('7a2ccb00-85c0-4d70-bf98-779524a73e0f')
    assert isinstance(target, mantiumapi.intelet.Intelet)
    assert target.name == 'Test Intelet'
    assert target.intelet_id == '7a2ccb00-85c0-4d70-bf98-779524a73e0f'
    assert target.organization_id == '55ef3083-6bb5-4794-bb5b-706f20597084'
    assert target.description == 'Test Intelet Description'
    assert target.created_at == '2021-01-01T00:00:00.000000+00:00'
    assert target.created_by == '31418670-2905-4875-ae36-02908bafaa52'
    assert target.updated_at == '2021-01-02T00:00:00.000000+00:00'


@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_intelet_execute(mock_post):
    target = mantiumapi.intelet.Intelet.from_id('7a2ccb00-85c0-4d70-bf98-779524a73e0f')
    target_result = target.execute('test input')
    assert isinstance(target_result, mantiumapi.execute.InteletExecution)
    assert target_result.intelet_execution_id == 'c638ce5f-67e2-4d99-8d28-b1535f41e55d'
    assert target_result.intelet_id == '7a2ccb00-85c0-4d70-bf98-779524a73e0f'
    assert target_result.status == 'QUEUED'
    assert target_result.input == 'test input'
    assert target_result.output == 'test output'
    assert target_result.error == 'error'
    assert target_result.reason == 'reason'
    assert isinstance(
        target_result.executed_prompts[0],
        mantiumapi.execute.PromptExecution,
    )
    assert target_result.pending_prompts == [
        '5a2ccb00-85c0-33dd-bf98-779524a73e0f',
        '4b823574-f963-45d4-9e17-1f26bdd612e0',
    ]
    assert target_result.executed_prompts[0].status == 'COMPLETED'
