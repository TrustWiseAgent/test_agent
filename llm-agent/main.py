
"""
conda create -n autogen python=3.11.4
conda activate autogen

pip install pyautogen litellm[proxy]

litellm --model ollama/mistral
litellm --model ollama/codellama
"""

import autogen

config_list_mistral = [
    {
        'base_url': "http://0.0.0.0:4000",
        'model': "ollama/mistral",
        'api_key' : "NULL"
    }
]

config_list_codellama= [
    {
        'base_url': "http://0.0.0.0:5000",
        'model': "ollama/codellama",
        'api_key' : "NULL"
    }
]

llm_config_mistral = {
    "config_list": config_list_mistral,
}

llm_config_codellama = {
    "config_list": config_list_codellama,
}

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config_mistral
)

coder = autogen.AssistantAgent(
    name="coder",
    llm_config=llm_config_codellama
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").strip().lower().endswith("terminate"),
    code_execution_config={"work_dir": "web", "use_docker": False},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satification,
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task2="""
Please search google and create code to last stock price for INTC, then run code.
"""

groupchat = autogen.GroupChat(agents=[user_proxy, coder, assistant], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_mistral)

user_proxy.initiate_chat(manager, message=task2)