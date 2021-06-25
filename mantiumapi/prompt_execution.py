from .client import orm_api

class PromptExecution:
    def __init__(self, prompt_execution_id, obj=''):
        self.prompt_execution_id = prompt_execution_id
        if obj:
            self.prompt_execution_id = obj['prompt_execution_id']
            self.prompt_id = obj['prompt_id']
            self.input = obj['output']
            self.output = obj['output']
            self.reason = obj['reason']
            self.status = obj['status']
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
            self.prompt_id = obj['intelet_id']
            self.input = obj['output']
            self.output = obj['output']
            self.reason = obj['reason']
            self.status = obj['status']
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