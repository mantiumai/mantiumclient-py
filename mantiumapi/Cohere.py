# Cohere Prompt Settings

from enum import Enum 

class DefaultEngine(Enum):
        """Must have a default engine"""
        shrimp = 'shrimp'
        otter = 'otter'
        seal = 'seal'
        shark ='shark'
        orca = 'orca'
   
class AiMethod(Enum):
        """Must have an endpoint (ai_method)"""
        generate = 'generate'
        choose_best = 'choose_best'
        likelihood = 'likelihood'
        embed = 'embed'  # only functional with shrimp or seal
        similarity = 'similarity'  # only functional with shrimp or seal

class Cohere(object):
    """
    default_engine: shrimp, otter, seal, shark, orca
    ai_method: generate, choose_best, likelihood, embed, similarity 

    ***Settings***

    GENERATION: 
    max_tokens: type int, https://docs.cohere.ai/bpe-tokens-wiki/
    temperature: type float, https://docs.cohere.ai/temperature-wiki/
    k: optional, type int, default 0, only top k most likely tokens used for generation
    p: optional, type float, default .75, [0, 1] inclusive, probability
    frequencty_penalty: optional, type float, default 0, [0, 1] inclusive
    presence_penalty: optional, type float, default 0, [0, 1] inclusive 
    stop_sequences: optional, array of strings, cut generation at specified string value
    return_likelihoods: optional, one of GENERATION|ALL|NONE, default NONE
    -------------------------------------------------------------

    SIMILARITY:
    compares similarity of anchor string against target strings

    anchor: type str, used for comparison against targets
    targets: array of strings,  compared to anchor
    -------------------------------------------------------------

    CHOOSE BEST:
    uses log-likelihood to choose best option given probability

    query: type str, used to query against options
    options: array of strings, concatenates to the query
    mode: one of PREPEND_OPTION|APPEND_OPTION
        PREPEND_OPTION > P(query|option for option in options) > probability of query given option
        APPEND_OPTION > P(option for option in options|query) > probability of option given query
    -------------------------------------------------------------

    EMBEDDING:
    computes semantic infromation about the entirety of the input text
    https://docs.cohere.ai/embedding-wiki/

    text: array of strings

    embedding lengths by model:
    shrimp - 768
    otter - 1024
    seal - 1536
    -------------------------------------------------------------

    LIKELIHOOD:
    returns log-likelihood of every token in the input sequence and the sum of the likelihoods

    text: type str
    """

    def __init__(self, default_engine, ai_method):

        self.ai_provider = 'cohere'

        if not isinstance(default_engine, DefaultEngine):
            raise Exception("default_engine must be one of: shrimp|otter|seal|shark|orca")

        self.default_engine = default_engine.value

        if not isinstance(ai_method, AiMethod):
            raise Exception("ai_method must be: generate|choose_best|likelihood|embed|similarity")

        self.ai_method = ai_method.value










# # Choose Best
# export interface ChooseBestPromptParametersInterface {
#   basic_settings: ChooseBestPromptParametersBasicSettingsInterface;
#   default_engine: string;
# }

# interface ChooseBestPromptParametersBasicSettingsInterface {
#   mode: string;
#   options: string[];
# }

# export type ChooseBestPromptAttributes = ChooseBestAttributes & DeployMetadata;

# interface ChooseBestAttributes {
#   ai_method: "Compare - Choose Best";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: ChooseBestPromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface ChooseBestCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "choose-best";
#   ai_provider: string;
#   query: string;
#   mode: string;
#   options: string[];
# }

# # Embed
# export interface EmbedPromptParametersInterface {
#   basic_settings: EmbedPromptParametersBasicSettingsInterface;
#   default_engine: string;
# }

# interface EmbedPromptParametersBasicSettingsInterface {
#   texts: string[];
# }

# export type EmbedPromptAttributes = EmbedAttributes & DeployMetadata;

# interface EmbedAttributes {
#   ai_method: "Comprehend - Embed";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: EmbedPromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface EmbedCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "embed";
#   ai_provider: string;
#   texts: string[];
# }
# # Generate 
# export interface GeneratePromptParametersInterface {
#   basic_settings: GeneratePromptParametersBasicSettingsInterface;
#   default_engine: string;
# }

# interface GeneratePromptParametersBasicSettingsInterface {
#   k: number;
#   p: number;
#   max_tokens: number;
#   temperature: number;
#   frequency_penalty: number;
#   presence_penalty: number;
#   stop_sequences: string[];
#   return_likelihoods: "GENERATION" | "NONE" | "ALL";
# }

# export type GeneratePromptAttributes = GenerateAttributes & DeployMetadata;

# interface GenerateAttributes {
#   ai_method: "Compose - Generate";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: GeneratePromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface GenerateCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "generate";
#   ai_provider: string;
#   prompt: string;
#   k: number;
#   p: number;
#   max_tokens: number;
#   temperature: number;
#   frequency_penalty: number;
#   presence_penalty: number;
#   stop_sequences: string[];
#   return_likelihoods: "GENERATION" | "NONE" | "ALL";
# }
# # Likelihood
# export interface LikelihoodPromptParametersInterface {
#   basic_settings: LikelihoodPromptParametersBasicSettingsInterface;
#   default_engine: string;
# }

# interface LikelihoodPromptParametersBasicSettingsInterface {
#   text: string;
# }

# export type LikelihoodPromptAttributes = LikelihoodAttributes & DeployMetadata;

# interface LikelihoodAttributes {
#   ai_method: "Comprehend - Likelihood";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: LikelihoodPromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface LikelihoodCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "likelihood";
#   ai_provider: string;
#   text: string;
# }
# # Similarity
# export interface SimilarityPromptParametersInterface {
#   basic_settings: SimilarityPromptParametersBasicSettingsInterface;
#   default_engine: string;
# }

# interface SimilarityPromptParametersBasicSettingsInterface {
#   anchor: string;
#   targets: string[];
# }

# export type SimilarityPromptAttributes = SimilarityAttributes & DeployMetadata;

# interface SimilarityAttributes {
#   ai_method: "Compare - Similarity";
#   ai_provider: string;
#   created_at: string;
#   ai_engine_id: string;
#   description: string;
#   last_activity: string;
#   name: string;
#   prompt_id: string;
#   prompt_parameters: SimilarityPromptParametersInterface;
#   prompt_text: string;
#   status: string;
# }

# export interface SimilarityCurlResponseAttributesInterface {
#   endpoint: string;
#   ai_method: "similarity";
#   ai_provider: string;
#   anchor: string;
#   targets: string[];
# }