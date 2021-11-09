"""Mantium Prompts"""

from .engine_id_values import default_ai_engines
from .utils import get_engine_id
from .prompt import Prompt
from enum import Enum


class DefaultEngine(str, Enum):
    """Must have a default engine, constrained to engines available to Mantium."""

    iron = 'iron'


class AiMethod(str, Enum):
    """Must have an endpoint (ai_method), constrained to engines available to Mantium."""

    wordsmith = 'Wordsmith'


class Mantium(Prompt):
    """
    Mantium Prompt class, inherits from Prompt.
    Required parameters: default_engine, ai_method

    default_engine: iron
    ai_method: Wordsmith

    ***Settings***
    maxTokens: Max 2048 (incl. input)
    temperature: [0,1] inclusive
    topP: [0,1] inclusive

    ***Example Prompt Instance***
    mantium_prompt = Mantium(default_engine=DefaultEngine.iron, ai_method = AiMethod.Wordsmith)
    """

    def __init__(self, default_engine, ai_method):

        self.ai_provider = 'ai21'

        if not isinstance(default_engine, DefaultEngine):
            raise Exception('default_engine must be one of: DefaultEngine. + iron')

        self.default_engine = default_engine.value
        self.ai_engine_id = get_engine_id(self.default_engine)

        if not isinstance(ai_method, AiMethod):
            raise Exception('ai_method must be: complete')

        self.ai_method = ai_method.value
