"""OpenAI Prompts"""

from enum import Enum


class DefaultEngine(str, Enum):
    """Must have a default engine, constrained to engines available to OpenAI."""

    davinci = 'davinci'
    curie = 'curie'
    babbage = 'babbage'
    ada = 'ada'


class AiMethod(str, Enum):
    """Must have an endpoint (ai_method), constrained to engines available to OpenAI."""

    completions = 'completions'
    search = 'search'
    classifications = 'classifications'
    answers = 'answers'


class OpenAi(Prompt):

    """
    OpenAI Prompt class, inherits from Prompt.
    Required parameters: default_engine, ai_method

    default_engine: davinci, curie, babbage, ada, davinci-codex, cushman-codex
    ai_method: completions, search, classifications, answers, codex

    ***Settings***
    maxTokens: Max 2048 (incl. input)
    temperature: [0,1] inclusive
    topP: [0,1] inclusive

    ***Example Prompt Instance***
    openai_prompt = OpenAi(default_engine=DefaultEngine.davinci, ai_method = AiMethod.classifications)

    """

    ai_provider = 'openai'

    def __init__(self, default_engine, ai_method):

        if not isinstance(default_engine, DefaultEngine):
            raise Exception('default_engine must be one of: j1_jumbo|j1_large')

        self.default_engine = default_engine.value
        self.ai_engine_id = get_engine_id(default_engine.value)

        if not isinstance(ai_method, AiMethod):
            raise Exception('ai_method must be: complete')

        self.ai_method = ai_method.value
