from config import API_KEY, MODEL_NAME, BASE_URL
from llm.client import LLMClient


client = LLMClient(
    API_KEY,
    MODEL_NAME,
    BASE_URL
)

messages = [
    {
        "role": "system",
        #给模型的全局行为指令
        "content": "You are a helpful research assistant."
    },
    {
        "role": "user",
        #用户提出的问题
        "content": "What is an AI agent? Answer briefly."
    }
]

reply = client.chat(messages)

print("模型回答：", reply)
#client.chat(messages)--进入 LLMCLient.chat()
#构造headers--构造data--requests.post()--Moonshot--response--raise_for_status
#提取 content- return reply
