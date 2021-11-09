# AI21 Prompt Settings
# Completion

from .prompt import Prompt
from .engine_id_values import default_ai_engines
from enum import Enum


def get_engine_id(engine_name):
    """Get Engine ID value from engine_id_values."""

    engine_id = next(engine for engine in default_ai_engines if engine['name'] == engine_name)
    return engine_id if engine_id else None


class DefaultEngine(str, Enum):
    """Must have a default engine, constrained to engines available to AI21."""

    j1_jumbo = 'j1_jumbo'
    j1_large = 'j1_large'


class AiMethod(Enum):
    """Must have an endpoint (ai_method), constrained to endpoints available to AI21."""

    complete = 'complete'


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

    def __init__(self, default_engine, ai_method):

        if not isinstance(default_engine, DefaultEngine):
            raise Exception('default_engine must be one of: j1_jumbo|j1_large')

        self.default_engine = default_engine.value
        self.ai_engine_id = get_engine_id(self.default_engine)

        if not isinstance(ai_method, AiMethod):
            raise Exception('ai_method must be: complete')

        self.ai_method = ai_method.value


# interface CompletePromptParametersBasicSettingsInterface {
#   maxTokens: number;
#   numResults: number;
#   temperature: number;
#   topKReturn: number;
#   topP: number;
#   stopSequences: string[];
# }

# export type CompletePromptAttributes = CompleteAttributes & DeployMetadata;

# interface CompleteAttributes {
#   ai_method: "complete";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: CompletePromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface CompleteCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "complete";
#   ai_provider: string;
#   prompt: string;
#   maxTokens: number;
#   numResults: number;
#   temperature: number;
#   topKReturn: number;
#   topP: number;
#   stopSequences: string[];
# }
