# -*- coding: utf-8 -*-
#  Copyright (c) 2021 Mantium, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# Please refer to our terms for more information:
#     https://mantiumai.com/terms-of-use/
#
from mantiumapi.log import Log
from mantiumapi import Prompt, Intelet, Tag, PromptExecution, InteletExecution, prompt_execution
import time


def check_result(cls, id):
    while True:
        result = cls.get_result(id)
        print(result)
        if result['status'] == 'RECEIVED':
            time.sleep(5)
        elif result['status'] == 'QUEUED':
            time.sleep(5)
        elif result['status'] == 'RUNNING':
            time.sleep(5)
        elif result['status'] == 'REJECTED':
            return 'REJECTED'
        elif result['status'] == 'ERROR':
            return 'ERROR'
        elif result['status'] == 'INTERRUPTED':
            # Interrupted for HITL
            return 'INTERRUPTED'
        else:
            result['status'] == 'COMPLETED'
            return result


print('-----------')

# Get list of Intelets
'''
intelets = Intelet.get_list()
for i in intelets:
    print(i.name)
    print(i.description)
    print(i.prompts)
'''

# Creating new Intelet
'''
new_intelet = Intelet()
new_intelet.description = "This is a new intelet"
new_intelet.name = "This is a new intelet"
new_intelet.save()
'''

# Inserting a Prompt into an Intelet
'''
intelet.description = "new description 2"
intelet.prompts.insert(0,prompt)
'''

# Execute Intelet and get result
'''
intelet = Intelet.from_id('7c3a14f3-aeaa-468b-9b8f-8d8a053f1719')
intelet_execute = intelet.execute('34')
print(intelet_execute)
'''

# Get Intelet Execution Status
'''
intelet_execution = InteletExecution('9095c561-7245-4bef-8d79-f36d5216c6c4')
print(intelet_execution.executed_prompts)
for p in intelet_execution.executed_prompts:
    print("Prompt execution id: ", p.prompt_id)
    print("Prompt execution status: ", p.status)
    print("Prompt execution reason: ", p.reason)
    print("Prompt execution HITL info: ", p.hitl_info)
    if p.status == 'INTERRUPTED':
        p.hitl_accept()
'''

# Creating new Prompt
'''
new_prompt = Prompt()
new_prompt.prompt_text = "I am a new prompt"
new_prompt.name = "prompt 46"
new_prompt.description = "New prompt description"
new_prompt.ai_method = "completion"
new_prompt.ai_provider = "OpenAI"
new_prompt.default_engine = "ada"
new_prompt.prompt_parameters = {
    "basic_settings": {
        "top_p": "1",
        "stop_seq": [
            "\n"
        ],
        "max_tokens": 16,
        "temperature": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0
    },
    "advanced_settings": {
        "n": "1",
        "echo": "true",
        "stream": "true",
        "best_of": "1",
        "logprobs": "1",
        "logit_bias": []
    }
}
new_prompt.status = "ACTIVE"
new_prompt.save()
'''

# Get list of Prompts

prompts = Prompt.get_list()
for p in prompts:
    print('--------')
    print("prompt: ", p.id, p.description)
    #for i in p.intelets:
    #    print("intelet: ", i.id, i.name)

# Get Prompt
'''
prompt = Prompt.from_id('6004bfd0-5bee-4f46-bd89-1e4a6ca3f76b')
print(prompt.name)
print(prompt.intelets)
print(prompt.tags)
'''

# Execute Prompt and get result
'''
prompt = Prompt.from_id('6004bfd0-5bee-4f46-bd89-1e4a6ca3f76b')
prompt_execute = prompt.execute('10 15 20 30')
#execute_id = prompt_execute['prompt_execution_id']
#result = check_result(Prompt, execute_id)
#print(result)
#print(prompt_execute)
prompt_execute.refresh()
print(prompt_execute.status)
'''

# Get all HITL prompts
'''
hitl_prompts = PromptExecution.get_list_hitl()
for p in hitl_prompts:
    print(p.prompt_execution_id)
    print(p.status)
    print(p.reason)
    print(p.hitl_info)
'''

# Get prompt execution status
'''
prompt_execute = PromptExecution(prompt_execution_id='cf74e5b5-bedd-48dc-a543-c6aaebdd279e')
print(prompt_execute.status)
print(prompt_execute.output)
print(prompt_execute.reason)
print(prompt_execute.hitl_info)
'''

# Get prompt execution result and HITL
'''
prompt_execute = PromptExecution(prompt_execution_id='b23534c5-b25e-4bd9-9f43-15f0775b93c8')
print(prompt_execute.status)
print(prompt_execute.output)
print(prompt_execute.reason)
prompt_execute.hitl_accept()
print(prompt_execute.status)
'''

# HITL modify output
'''
prompt_execute = PromptExecution(prompt_execution_id='30e21507-09c3-4f19-a08e-78e368dd497e')
print(prompt_execute.output)
prompt_execute.hitl_modify_output(new_output="This is the new output")
print(prompt_execute.status)
print(prompt_execute.output)
'''

# HITL modify input
'''
prompt_execute = PromptExecution(prompt_execution_id='cf74e5b5-bedd-48dc-a543-c6aaebdd279e')
print(prompt_execute.output)
prompt_execute.hitl_modify_input(new_input="This is the new input")
print(prompt_execute.status)
print(prompt_execute.output)
'''


# Update a prompt
'''
prompt = Prompt.from_id('77739d23-6ace-439c-8feb-e1e34afc5c0c')
prompt.description = "Updated description"
prompt.tags.append('edeea6c8-5f00-4c79-870a-575e1bb1dc4e')
prompt.save()
'''

# Add intelet to prompt
'''
intelet = Intelet.from_id('7a198398-ff8b-4df3-8806-5e16f8083a51')
prompt = Prompt.from_id('77739d23-6ace-439c-8feb-e1e34afc5c0c')
prompt.description = "No new intelets"
prompt.save()
'''

### Tags don't currently work

# Get Tags
'''
tags = Tag.get_list()
for t in tags:
    print(t.id, t.name)
'''

# Create Tag
'''
tag = Tag()
tag.name = "It"
tag.description = "Who's it?"
tag.save()
'''

'''
# Get logs
logs = Log.get_list()
'''
