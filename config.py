import os
#获取环境变量
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("MOONSHOT_API_KEY")
# env环境里的变量名字
MODEL_NAME = "kimi-k2.6"

BASE_URL = "https://api.moonshot.cn/v1/chat/completions"
#集中管理
#.env 放敏感信息，和运行环境有关的信息
#config放程序内部统一访问配置的位置