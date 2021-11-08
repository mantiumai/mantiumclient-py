# Mantium Prompt Settings

from enum import Enum


class DefaultEngine(Enum):
    """Must have a default engine"""

    iron = 'iron'


class AiMethod(Enum):
    """Must have an endpoint (ai_method)"""

    wordsmith = 'Wordsmith'


class Mantium(object):
    """
    default_engine: j1_jumbo, j1_large
    ai_method: complete

    ***Settings***
    maxTokens: Max 2048 (incl. input)
    temperature: [0,1] inclusive
    topP: [0,1] inclusive"""

    def __init__(self, default_engine, ai_method):

        self.ai_provider = 'ai21'

        if not isinstance(default_engine, DefaultEngine):
            raise Exception('default_engine must be one of: DefaultEngine. + iron')

        self.default_engine = default_engine.value

        if not isinstance(ai_method, AiMethod):
            raise Exception('ai_method must be: complete')

        self.ai_method = ai_method.value


# export interface WordsmithPromptParametersInterface {
#   basic_settings: WordsmithPromptParametersBasicSettingsInterface;
#   default_engine: string;
# }

# interface WordsmithPromptParametersBasicSettingsInterface {
#   temperature: number;
#   top_p: number;
# }

# export type WordsmithPromptAttributes = WordsmithAttributes & DeployMetadata;

# interface WordsmithAttributes {
#   ai_method: "Wordsmith";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: WordsmithPromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface WordsmithCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "wordsmith";
#   ai_provider: string;
#   context: string;
#   temp: number;
#   top_p: number;
# }
