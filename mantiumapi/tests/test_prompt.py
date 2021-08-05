import unittest
from unittest import mock

import mantiumapi.prompt


def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.content = data
            self.json_data = data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if (
        args[0] == 'GET'
        and args[1]
        == 'https://api.mantiumai.com/v1/prompt/9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4'
    ):
        return MockResponse(PROMPT, 200)
    elif (
        args[0] == 'GET'
        and args[1]
        == 'https://api.mantiumai.com/v1/prompt/result/23d8a134-0fee-4da5-a1ae-c78ea569d0ed'
    ):
        return MockResponse(PROMPT_EXECUTE_RESULT, 200)
    elif (
        args[0] == 'POST'
        and args[1]
        == 'https://api.mantiumai.com/v1/prompt/9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4/execute'
    ):
        return MockResponse(PROMPT_EXECUTE, 200)
    else:
        return MockResponse('', 404)


class PromptTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch(
        'jsonapi_requests.request_factory.requests.request',
        side_effect=mocked_requests,
    )
    def test_prompt(self, mock_get):
        target = mantiumapi.prompt.Prompt.from_id(
            '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4'
        )
        self.assertIsInstance(target, mantiumapi.prompt.Prompt)
        self.assertEqual(target.name, 'Test Prompt')
        self.assertEqual(
            target.prompt_id, '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4'
        )
        self.assertEqual(
            target.organization_id, 'a448a888-6faf-4b7f-8f57-3f6872036428'
        )
        self.assertEqual(target.description, 'Test Prompt Description')
        self.assertEqual(target.created_at, '2021-01-01T00:00:00.000000+00:00')
        self.assertEqual(
            target.last_activity, '2021-01-02T00:00:00.000000+00:00'
        )
        self.assertEqual(target.prompt_text, 'test prompt text')
        self.assertEqual(target.ai_method, 'completion')
        self.assertEqual(target.ai_provider, 'OpenAI')
        self.assertEqual(target.default_engine, 'davinci')
        self.assertEqual(target.status, 'ACTIVE')
        self.assertDictEqual(
            target.prompt_parameters,
            dict(
                {
                    'basic_settings': {
                        'top_p': '1',
                        'stop_seq': ['\n'],
                        'max_tokens': '128',
                        'temperature': '1',
                        'presence_penalty': '0',
                        'frequency_penalty': '0',
                    },
                    'advanced_settings': {
                        'n': '1',
                        'echo': 'false',
                        'stream': 'false',
                        'best_of': 1,
                        'logprobs': '1',
                        'logit_bias': [],
                    },
                }
            ),
        )

    @mock.patch(
        'jsonapi_requests.request_factory.requests.request',
        side_effect=mocked_requests,
    )
    def test_prompt_execute(self, mock_post):
        target = mantiumapi.prompt.Prompt.from_id(
            '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4'
        )
        target_result = target.execute('test input')
        self.assertEqual(
            target_result.prompt_execution_id,
            '23d8a134-0fee-4da5-a1ae-c78ea569d0ed',
        )
        self.assertEqual(
            target_result.prompt_id, '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4'
        )
        self.assertEqual(target_result.status, 'COMPLETED')
        self.assertEqual(target_result.input, 'test input')
        self.assertEqual(target_result.output, 'test output')
        self.assertEqual(target_result.error, '')
        self.assertEqual(target_result.reason, '')
        self.assertEqual(target_result.hitl_info, 'null')
        self.assertEqual(target_result.warning_message, '')


PROMPT = {
    'data': {
        'id': '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4',
        'type': 'prompt',
        'attributes': {
            'prompt_id': '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4',
            'organization_id': 'a448a888-6faf-4b7f-8f57-3f6872036428',
            'name': 'Test Prompt',
            'description': 'Test Prompt Description',
            'created_at': '2021-01-01T00:00:00.000000+00:00',
            'prompt_text': 'test prompt text',
            'ai_method': 'completion',
            'ai_provider': 'OpenAI',
            'default_engine': 'davinci',
            'status': 'ACTIVE',
            'prompt_parameters': {
                'basic_settings': {
                    'top_p': '1',
                    'stop_seq': ['\n'],
                    'max_tokens': '128',
                    'temperature': '1',
                    'presence_penalty': '0',
                    'frequency_penalty': '0',
                },
                'advanced_settings': {
                    'n': '1',
                    'echo': 'false',
                    'stream': 'false',
                    'best_of': 1,
                    'logprobs': '1',
                    'logit_bias': [],
                },
            },
            'last_activity': '2021-01-02T00:00:00.000000+00:00',
        },
        'relationships': {
            'intelets': {
                'data': [
                    {
                        'type': 'intelet',
                        'id': 'ea16149d-1a2e-4e59-ab50-591dd7411ab5',
                    }
                ]
            },
            'tags': {'data': []},
            'security_policies': {'data': []},
            'prompt_policies': {'data': []},
        },
    },
    'included': [
        {
            'id': 'ea16149d-1a2e-4e59-ab50-591dd7411ab5',
            'type': 'intelet',
            'attributes': {
                'intelet_id': 'ea16149d-1a2e-4e59-ab50-591dd7411ab5',
                'name': 'intelet 1',
            },
            'relationships': {},
        }
    ],
    'meta': {},
    'links': {},
}

PROMPT_EXECUTE = {
    'success': 'true',
    'prompt_id': '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4',
    'input': 'test',
    'status': 'QUEUED',
    'prompt_execution_id': '23d8a134-0fee-4da5-a1ae-c78ea569d0ed',
    'error': '',
    'warning_message': '',
}

PROMPT_EXECUTE_RESULT = {
    'prompt_execution_id': '23d8a134-0fee-4da5-a1ae-c78ea569d0ed',
    'prompt_id': '9001cf88-eaec-485c-8fcd-1d9fe3ba0ac4',
    'status': 'COMPLETED',
    'input': 'test input',
    'output': 'test output',
    'error': '',
    'reason': '',
    'hitl_info': 'null',
    'warning_message': '',
}
