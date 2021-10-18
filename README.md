## Mantium API Client Library

[![Build Status](https://travis-ci.com/mantiumai/mantiumclient-py.svg?branch=main)](https://travis-ci.com/mantiumai/mantiumclient-py)

---

## Table of Contents
- [Quickstart](#quickstart)
- [Authentication](#authentication)
- [Installation](#installation)
- [Usage](#usage)
  - [Initializing](#initializing)
  - [Auth](#auth)
    - [Login](#login)
    - [Logout](#logout)
  - [AI Methods](#ai-methods)
    - [List Methods](#list-methods)
  - [AI Engines](#ai-engines)
    - [Get All AI Engines](#get-all-ai-engines)
    - [Get Ai Engines By Provider](#get-ai-engines-by-provider)
    - [Get Ai Engine By Name](#get-ai-engine-by-name)
  - [Tags](#tags)
    - [List Tags](#list-tags)
    - [Get Tag by ID](#get-tag-by-id)
    - [Create Tag](#create-tag)
    - [Update Tag](#update-tag)
    - [Delete Tag](#delete-tag)
  - [Prompts](#prompts)
    - [List Prompts](#list-prompts)
    - [Create Prompt](#create-prompt)
    - [Update Prompt](#update-prompt)
    - [Get Prompt by ID](#get-prompt-by-id)
    - [Delete Prompt](#delete-prompt)
    - [Execute Prompt](#execute-prompt)
  - [Intelets](#intelets)
    - [List Intelets](#list-intelets)
    - [Create Intelet](#create-intelet)
    - [Update Intelet](#update-intelet)
    - [Get Intelet by ID](#get-intelet-by-id)
    - [Delete Intelet](#delete-intelet)
    - [Execute Intelet](#execute-intelet)
  - [Logs](#logs)
    - [List Logs](#list-logs)
    - [Get Log by ID](#get-log-by-id)

## Quickstart:
Read the [getting started guide](https://developer.mantiumai.com/docs) for more information on how to use Mantium.
## Authentication
- Make an account by visiting [app.mantiumai.com](https://app.mantiumai.com) and select Register.
- Enter your email address and create a password. After you've verified the email, you'll be able to sign in to the Mantium application. You'll also need your username and password to obtain a token for API use.

## Installation
To install the python Library please use the following command.

```bash
pip install mantiumapi
```
## Usage

Set authentication credentials in your environment. Setting MANTIUM_USER and MANTIUM_PASSWORD will
allow the client to obtain the authentication token, which will re-authenticate when the token expires.

It's also possible to directly set the token through the MANTIUM_TOKEN environment variable. Documentation for authenticating can be found [here](https://developer.mantiumai.com/reference#access_token_login_v1_auth_login_access_token_post)

+ Linux/MacOS
```bash
export MANTIUM_USER='<username>'
export MANTIUM_PASSWORD='<password>'
```
+ Windows
```Batchfile
set MANTIUM_USER="<username>"
set MANTIUM_PASSWORD="<password>"
```
+ Windows Powershell
```Powershell
$env:MANTIUM_USER="<username>"
$env:MANTIUM_PASSWORD="<password>"
```

---
### AI Methods
Get all of the supported ai_methods for a provider
#### List Methods

Requires AI Provider name 

```python
>>> from mantiumapi import AiMethods
>>> ai_methods = AiMethods.get_list("openai")
>>> print([method.name for method in ai_methods])
['answers', 'classifications', 'completion', 'search']
```

---
### AI Engines
Get available AI engines

#### Get All AI Engines
Get all of the configured and available AI engines

```python
>>> from mantiumapi import AiEngine
>>> ai_engines = AiEngine.get_list()
>>> print([(engine.ai_provider, engine.name) for engine in ai_engines])
[('OpenAI', 'content-filter-alpha-c4'), ...]
```

#### Get Ai Engines for a single provider
```python
>>> ai_engines = AiEngine.from_provider("Cohere")
>>> print([(engine.ai_provider, engine.name) for engine in ai_engines])
[('Cohere', 'baseline-otter'), ...]
```
[Go to Table of Contents](#table-of-contents)

---
### Tags

#### List Tags

Get all of the tags for your selected organization.

Query Params
`Page` Page number
`Size` Page size. If not supplied, returns all the results in a single page for certain APIs.

```Python
>>> from mantiumapi import Tag
>>> tags = Tag.get_list()
>>> print([tag.name for tag in tags])
['Tag 1', 'Tag 2']
```
Passing URL parameters
```python
>>> tags = Tag.get_list(params={"page":1,"size":1})
>>> print([tag.name for tag in tags])
['Tag 1']
```
#### Get Tag by ID
```python
>>> tag = Tag.from_id('8c809efe-4738-4c7a-93e1-ea933ef84172')
>>> tag.name
['Tag 1']
```

#### Create Tag

```python
>>> new_tag = Tag()
>>> new_tag.name = "My new tag"
>>> new_tag.description = "This is a new tag"
>>> new_tag.create()
```

#### Update Tag
```python
>>> tag = Tag.from_id('8c809efe-4738-4c7a-93e1-ea933ef84172')
>>> tag.name = "New tag name"
>>> tag.save()
```

#### Delete Tag
```python
>>> tag = Tag.from_id('8c809efe-4738-4c7a-93e1-ea933ef84172')
>>> tag.refres()
>>> tag.delete()
```

[Go to Table of Contents](#table-of-contents)

---
### Prompts

#### List Prompts

List all of your organization's prompts. 

Optional Query String Parameters

- page - The page of records to return. Optional, defaults to page 1.
- size - the number of records to return for each page. Optional, defaults to 20 - prompts a page.
- schema_class - not used, exclude.
- tags - A list of Tag IDs separated by comma used to filter the results, optional.

[Document link](https://developer.mantiumai.com/reference#list_prompts_v1_prompt__get)

```python
>>> from mantiumapi import Prompt
>>> prompts = Prompt.get_list(params={"size":2})
>>> print([prompt.name for prompt in prompts])
['My first prompt', 'Test prompt']
```

#### Get Prompt by ID

```python
>>> prompt = Prompt.from_id('3184ba90-c2b1-4604-bbd2-6ed436ca5f52')
>>> prompt.name
'My first prompt'
```

#### Create Prompt


```python
>>> new_prompt.name = "A new prompt"
>>> new_prompt.prompt_text = "Prompt text"
>>> new_prompt.ai_provider = "OpenAI"
>>> new_prompt.default_engine = "davinci"
>>> new_prompt.ai_method = "completion"
>>> new_prompt.ai_engine_id = "b2ffecf7-4fee-42e7-b85d-a5e28d939396"
>>> new_prompt.text = "Prompt text"
>>> new_prompt.prompt_parameters = {"basic_settings": {"temperature": 1,"max_tokens": 16,"frequency_penalty": 0,"presence_penalty": 0,"top_p": 1},"advanced_settings": {"best_of": 1,"n": 1,"echo": "false","stream": "false"}}
>>> new_prompt.create()
```

#### Update Prompt
```python
>>> prompt = Prompt.from_id('3184ba90-c2b1-4604-bbd2-6ed436ca5f52')
>>> prompt.name = "New Prompt name"
>>> prompt.update()
```

#### Delete Prompt
```python
>>> prompt = Prompt.from_id('3184ba90-c2b1-4604-bbd2-6ed436ca5f52')
>>> prompt.refresh()
>>> prompt.delete()
```

#### Execute Prompt

Asynchronously submit input to a Prompt for execution. Returns a PromptExecute object to manage the result.

As this is an asynchronous endpoint, the first result returned will not be a finished result. The result can be updated by calling .refresh() on the PromptExecute object.

- Input (string)- Data to append to Prompt for execution

```python
>>> prompt = Prompt.from_id('0aab4c37-d931-4726-8768-b7ff91776ce6')
>>> result = Prompt.execute('Data for the Prompt')
>>> result.__dict__
{'prompt_execution_id': '221202da-9d76-4711-91f0-e0d8b50a57d5', 'prompt_id': '0aab4c37-d931-4726-8768-b7ff91776ce6', 'input': 'Data for the Prompt', 'output': '', 'reason': '', 'status': 'RUNNING', 'error': '', 'warning_message': '', 'hitl_info': None}
>>> result.refresh()
>>> result.refresh()
>>> result.__dict__
{'prompt_execution_id': '221202da-9d76-4711-91f0-e0d8b50a57d5', 'prompt_id': '0aab4c37-d931-4726-8768-b7ff91776ce6', 'input': 'Data for the Prompt', 'output': 'Output from the Prompt Exeuction', 'reason': '', 'status': 'COMPLETED', 'error': '', 'warning_message': '', 'hitl_info': None}
```

[Go to Table of Contents](#table-of-contents)

---

### Intelets
Intelets organize multiple prompts by grouping them together sequentially so that the output of one prompt feeds into the input of the next - this enables the creation of complex AI data pipelines for processing text.

#### List Intelets

List all of your organization's prompts. 

Optional Query String Parameters

- page - The page of records to return. Optional, defaults to page 1.
- size - the number of records to return for each page. Optional, defaults to 20 - prompts a page.

```python
>>> from mantiumapi import Intelet
>>> intelets = Intelet.get_list()
>>> print([i.name for i in intelets])
['My first Intelet', 'Processing pipeline', ...]
```

#### Get Intelet by ID

```python
>>> intelet = Intelet.from_id('0aab4c37-d931-4726-8768-b7ff91776ce6')
>>> print(intelet.name)
'My first Intelet'
```

#### Create Intelet

The order of Prompts in the prompts list dictate in which order they will be executed in the pipeline.

```python
>>> new_intelet=Intelet()
>>> new_intelet.name = "Name of new Intelet"
>>> new_intelet.description = "Description of the Intelet"
>>> new_intelet.prompts = ['3184ba90-c2b1-4604-bbd2-6ed436ca5f52']
>>> new_intelet.save()
```

#### Update Intelet
```python
>>> intelet = Intelet.from_id('3184ba90-c2b1-4604-bbd2-6ed436ca5f52')
>>> intelet.name = "New Intelet name"
>>> intelet.update()
```

#### Delete Intelet
```python
>>> intelet = intelet.from_id('3184ba90-c2b1-4604-bbd2-6ed436ca5f52')
>>> intelet.refresh()
>>> intelet.delete()
```

#### Execute Intelet

Asynchronously submit input to an Intelet for execution. Returns a InteletExecute object to manage the result.

As this is an asynchronous endpoint, the first result returned will not be a finished result. The result can be updated by calling .refresh() on the InteletExecute object.

- Input (string)- Data to append to Prompt for execution

```python
>>> intelet = Intelet.from_id('3c3a14f3-aeaa-468b-8b8f-8d8a053f1719')
>>> result = Intelet.execute('Sample input text')
>>> result.__dict__
{'intelet_execution_id': 'd81fba13-d3fc-41af-9f0b-10816b7ca5df', 'intelet_id': '3c3a14f3-aeaa-468b-8b8f-8d8a053f1719', 'input': 'Sample input text', 'output': '', 'reason': '', 'status': 'QUEUED', 'error': '', 'executed_prompts': [], 'pending_prompts': ['760311e5-9137-4ed6-dc2a-34f077b44131', '3a063314-1fe5-42f2-a276-c25404071c3d', '6004bfd0-5bec-4f41-bd89-1e4a6ca3f76b'], 'results': []}
>>> result.refresh()
>>> result.__dict__
{'intelet_execution_id': 'd81fba13-d3fc-41af-9f0b-10816b7ca5df', 'intelet_id': '3c3a14f3-aeaa-468b-8b8f-8d8a053f1719', 'input': 'Sample input text', 'output': 'Output of Intelet', 'reason': '', 'status': 'COMPLETED', 'error': '', 'executed_prompts': ['760311e5-9137-4ed6-dc2a-34f077b44131', '3a063314-1fe5-42f2-a276-c25404071c3d', '6004bfd0-5bec-4f41-bd89-1e4a6ca3f76b'], 'pending_prompts': [], 'results': []}
```

[Go to Table of Contents](#table-of-contents)

---

### Logs

#### List Logs

Query Params

* `page` (int) - Page number
* `size` (int) - Page size. If not supplied, returns all the results in a single page for certain APIs.
* `after_date` (string) - After Date
* `before_date` (string) Before Date
* `log_type` (string) LogType, An enumeration. [AUTH | DEFAULT | PROMPT | INTELET FILE]
* `log_level` (string) Log Level
* `log_status` (string) Log Status

```python
>>> from mantiumapi import Log
>>> logs = Log.get_list(params={"size":5, "log_type":"PROMPT"})
>>> print([(l.log_type, l.log_payload) for l in logs])
[('PROMPT', {'to': 'completion', 'name': 'OpenAI Completion', 'error': '', 'input': ...]
```

#### Get Log by ID

```python
>>> log = Log.from_id('b372d92c-028d-463b-98ba-3cec3f170af5')
>>> log.id
'b372d92c-028d-463b-98ba-3cec3f170af5'
>>> log.log_type
'PROMPT'
```

[Go to Table of Contents](#table-of-contents)

---

