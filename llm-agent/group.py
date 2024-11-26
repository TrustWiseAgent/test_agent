from autogen import config_list_from_json
import autogen

# 配置 api key
#config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
#llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 120}

config_list_mistral = [
    {
        'base_url': "https://api.link-ai.tech/v1",
        'model': "LinkAI-4o",
        'api_key' : "Link_O9AOyaYEBmCzzNGr2HkWqgJw3Hba8jGY3rOqVVsKdY"
    }
]

config_list_codellama= [
    {
        'base_url': "http://127.0.0.1:11434/v1",
        'model': "codellama",
        'api_key' : "NULL"
    }
]

config_list_gpt_4o = [
    {
        'base_url': "https://api.link-ai.tech/v1",
        'model': "LinkAI-4o",
        'api_key' : "Link_O9AOyaYEBmCzzNGr2HkWqgJw3Hba8jGY3rOqVVsKdY"
    }
]

llm_config_mistral = {
    "config_list": config_list_mistral,
}

llm_config_codellama = {
    "config_list": config_list_gpt_4o,
}

# 创建 user proxy agent, coder, product manager  三个不同的角色
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    human_input_mode="NEVER",
    system_message="A human admin who will give the idea and run the code provided by Coder.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat", "use_docker": False},  #最多接收的响应的数量
    llm_config=llm_config_mistral
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_codellama,
)

pm = autogen.AssistantAgent(
    name="product_manager",
    system_message="You will help break down the initial idea into a well scoped requirement for the coder; Do not involve in future conversations or error fixing",
    llm_config=llm_config_mistral,
)

# 创建 组 groupchat
groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, pm], messages=[])
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_mistral)

# 初始化 开始干活
user_proxy.initiate_chat(
    manager, message="Build a classic & basic pong game with 2 players in python")
