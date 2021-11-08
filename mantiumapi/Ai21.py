# AI21 Prompt Settings
# Completion

from .prompt import Prompt
from .ai_engines import ai_engines
from enum import Enum


class DefaultEngine(str, Enum):
    """Must have a default engine"""

    j1_jumbo = 'j1_jumbo'
    j1_large = 'j1_large'


class AiMethod(Enum):
    """Must have an endpoint (ai_method)"""

    complete = 'complete'


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
