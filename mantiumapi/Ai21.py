"""AI21 Prompts"""

from engine_id_values import default_ai_engines
from utils import get_engine_id
from prompt import Prompt
from enum import Enum


class DefaultEngine(str, Enum):
    """Must have a default engine, constrained to engines available to AI21."""

    j1_jumbo = 'j1_jumbo'
    j1_large = 'j1_large'


class AiMethod(str, Enum):
    """Must have an endpoint (ai_method), constrained to endpoints available to AI21."""

    complete = 'complete'


print(default_ai_engines)


class Ai21(Prompt):

    """
    AI21 Prompt class, inherits from Prompt.
    Required parameters: default_engine, ai_method

    default_engine options: j1_jumbo, j1_large
    ai_method options: complete

    ***Settings***
    maxTokens: Max 2048 (incl. input)
    temperature: [0,1] inclusive
    topP: [0,1] inclusive

    ***Example Prompt Instance***
    ai_21_prompt = Ai21(default_engine=DefaultEngine.j1_jumbo, ai_method=AiMethod.complete)

    """

    ai_provider = 'ai21'

    def __init__(self, default_engine: object, ai_method: object):

        if not isinstance(default_engine, DefaultEngine):
            raise Exception('default_engine must be one of: j1_jumbo|j1_large')

        self.default_engine = default_engine.value
        self.ai_engine_id = get_engine_id(self.default_engine)

        if not isinstance(ai_method, AiMethod):
            raise Exception('ai_method must be: complete')

        self.ai_method = ai_method.value
