from .prompt import Prompt
from enum import Enum


class DefaultEngine(str, Enum):
    """Must have a default engine"""

    davinci = 'davinci'
    curie = 'curie'
    babbage = 'babbage'
    ada = 'ada'


class AiMethod(Enum):
    """Must have an endpoint (ai_method)"""

    completions = 'completions'
    search = 'search'
    classifications = 'classifications'
    answers = 'answers'


class Ai21(Prompt):

    """
    default_engine: j1_jumbo, j1_large
    ai_method: complete

    ***Settings***
    maxTokens: Max 2048 (incl. input)
    temperature: [0,1] inclusive
    topP: [0,1] inclusive"""

    ai_provider = 'ai21'

    def __init__(self, default_engine, ai_method):

        if not isinstance(default_engine, DefaultEngine):
            raise Exception('default_engine must be one of: j1_jumbo|j1_large')

        self.default_engine = default_engine.value

        if not isinstance(ai_method, AiMethod):
            raise Exception('ai_method must be: complete')

        self.ai_method = ai_method.value
