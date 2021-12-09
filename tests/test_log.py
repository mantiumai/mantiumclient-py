from unittest import mock

from mantiumapi.log import Log

LOG = {
  "data": [
    {
      "id": "9b1a8459-e867-419e-944f-f241e46f2ae2",
      "type": "log",
      "attributes": {
        "log_id": "9b1a8459-e867-419e-944f-f241e46f2ae2",
        "event_timestamp": "2021-11-11T18:32:05.290321+00:00",
        "organization_id": "df3d8e89-50cb-48f9-a121-8c641c88fd99",
        "log_type": "PROMPT",
        "log_payload": {
          "to": "Compose - Generate",
          "name": "Test Prompt",
          "error": "",
          "input": "In summary, ",
          "config": {
            "k": 0,
            "p": 0.4,
            "model": "baseline-orca",
            "prompt": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.\nIn summary, ",
            "max_tokens": 45,
            "temperature": 0,
            "stop_sequences": [],
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "return_likelihoods": "NONE"
          },
          "output": "\nJupiter is the largest planet in the Solar System, and the largest planet in the Solar System as measured by mass. It is the only planet in the Solar System with a substantial atmosphere, and the only planet in the",
          "status": "COMPLETED",
          "ai_app_id": 'null',
          "ai_method": "Compose - Generate",
          "direction": "incoming",
          "prompt_id": "c03d4397-c93d-450d-84b3-e68ae34641e4",
          "intelet_id": 'null',
          "ai_provider": "Cohere",
          "prompt_text": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.\n",
          "warning_message": 'null',
          "provider_response": {
            "text": "\nJupiter is the largest planet in the Solar System, and the largest planet in the Solar System as measured by mass. It is the only planet in the Solar System with a substantial atmosphere, and the only planet in the"
          },
          "input_character_length": 642
        },
        "log_level": "INFO"
      },
      "relationships": {}
    }
  ],
  "included": [],
  "meta": {},
  "links": {
    "total_items": 9,
    "current_page": 1
  }
}


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
        == 'https://api.mantiumai.com/v1/log'
    ):
        return MockResponse(LOG, 200)
    else:
        return MockResponse('', 404)
    
@mock.patch(
    'jsonapi_requests.request_factory.requests.request',
    side_effect=mocked_requests,
)
def test_log(mock_get):
    target = Log.get_list()
    assert isinstance(target[0], Log)
    assert target[0].log_id == '9b1a8459-e867-419e-944f-f241e46f2ae2'
    assert target[0].organization_id == 'df3d8e89-50cb-48f9-a121-8c641c88fd99'
    assert target[0].log_type == 'PROMPT'
    assert target[0].log_payload == {
          "to": "Compose - Generate",
          "name": "Test Prompt",
          "error": "",
          "input": "In summary, ",
          "config": {
            "k": 0,
            "p": 0.4,
            "model": "baseline-orca",
            "prompt": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.\nIn summary, ",
            "max_tokens": 45,
            "temperature": 0,
            "stop_sequences": [],
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "return_likelihoods": "NONE"
          },
          "output": "\nJupiter is the largest planet in the Solar System, and the largest planet in the Solar System as measured by mass. It is the only planet in the Solar System with a substantial atmosphere, and the only planet in the",
          "status": "COMPLETED",
          "ai_app_id": 'null',
          "ai_method": "Compose - Generate",
          "direction": "incoming",
          "prompt_id": "c03d4397-c93d-450d-84b3-e68ae34641e4",
          "intelet_id": 'null',
          "ai_provider": "Cohere",
          "prompt_text": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.\n",
          "warning_message": 'null',
          "provider_response": {
            "text": "\nJupiter is the largest planet in the Solar System, and the largest planet in the Solar System as measured by mass. It is the only planet in the Solar System with a substantial atmosphere, and the only planet in the"
          },
          "input_character_length": 642
        }
    assert target[0].log_level == 'INFO'

