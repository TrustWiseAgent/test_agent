from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample

"""
config_list = [
    {
        'base_url': "https://api.link-ai.tech/v1",
        'model': "LinkAI-4o",
        'api_key' : "Link_O9AOyaYEBmCzzNGr2HkWqgJw3Hba8jGY3rOqVVsKdY"
    }
]


config_list = [
    {
        'base_url': "https://api.link-ai.tech/v1",
        'model': "claude-3-5-sonnet",
        'api_key' : "Link_O9AOyaYEBmCzzNGr2HkWqgJw3Hba8jGY3rOqVVsKdY"
    }
]

"""
config_list = [
    {
        'base_url': "http://127.0.0.1:11434/v1",
        'model': "qwen2",
        'api_key' : "Link_O9AOyaYEBmCzzNGr2HkWqgJw3Hba8jGY3rOqVVsKdY"
    }
]


# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]
assistant = AssistantAgent(
    "assistant",
    llm_config={"config_list": config_list}
    )
user_proxy = UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(
    assistant,
    message="请画出前6个月上证指数的股票价格.")
# This initiates an automated chat between the two agents to solve the task