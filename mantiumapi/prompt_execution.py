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
from .client import orm_api

class PromptExecution:
    def __init__(self, prompt_execution_id, obj=''):
        self.prompt_execution_id = prompt_execution_id
        if obj:
            self.prompt_execution_id = obj['prompt_execution_id']
            self.prompt_id = obj['prompt_id']
            self.input = obj['input']
            self.output = obj['output']
            self.reason = obj['reason']
            self.status = obj['status']
            self.error = obj['error']
            if 'warning_message' in obj:
                self.warning_message = obj['warning_message']
            else:
                self.warning_message = ''
            if 'hitl_info' in obj:
                self.hitl_info = obj['hitl_info']
            else:
                self.hitl_info = '{}'
                
        if not hasattr(self, 'status'):
            self.refresh()

    @classmethod
    def get_list_hitl(cls):
        result = []
        get_path = f'hitl/'
        api_response = orm_api.endpoint(get_path).get()
        for object in api_response.payload:
            new = cls(prompt_execution_id=object['prompt_execution_id'], obj=object)
            result.append(new)
        return result

    def refresh(self):
        get_path = f'prompt/result/{self.prompt_execution_id}'
        api_response = orm_api.endpoint(get_path).get()
        self.__init__(prompt_execution_id=api_response.payload['prompt_execution_id'], obj=api_response.payload)

    def hitl_accept(self):
        post_path = f'hitl/{self.prompt_execution_id}/accept'
        orm_api.endpoint(post_path).post()
        self.refresh()

    def hitl_reject(self):
        post_path = f'hitl/{self.prompt_execution_id}/reject'
        orm_api.endpoint(post_path).post()
        self.refresh()

    def hitl_modify_output(self, new_output):
        post_path = f'hitl/{self.prompt_execution_id}/modify_output'
        orm_api.endpoint(post_path).post(json={'new_output': new_output})
        self.refresh()

    def hitl_modify_input(self, new_input):
        post_path = f'hitl/{self.prompt_execution_id}/modify_input'
        orm_api.endpoint(post_path).post(json={'new_input': new_input})
        self.refresh()


class InteletExecution:

    def __init__(self, intelet_execution_id, obj=''):
        self.intelet_execution_id = intelet_execution_id
        if obj:
            self.intelet_execution_id = obj['intelet_execution_id']
            self.intelet_id = obj['intelet_id']
            self.input = obj['input']
            self.output = obj['output']
            self.reason = obj['reason']
            self.status = obj['status']
            self.error = obj['error']
            self.executed_prompts = []
            self.pending_prompts = obj['pending_prompts']
            self.results = obj['results']

            for prompt in obj['executed_prompts']:
                p = PromptExecution('prompt_execution_id', obj=prompt)
                self.executed_prompts.append(p)

        if not hasattr(self, 'status'):
            self.refresh()

    def refresh(self):
        get_path = f'intelet/result/{self.intelet_execution_id}'
        api_response = orm_api.endpoint(get_path).get()
        self.__init__(intelet_execution_id=api_response.payload['intelet_execution_id'], obj=api_response.payload)