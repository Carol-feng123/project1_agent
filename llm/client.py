import requests
class LLMClient:
    def __init__(self,api_key,model_name,base_url):
        self.api_key=api_key
        self.model_name = model_name
        self.base_url = base_url
    def chat(self, messages):
        headers={
            "Authorization":"Bearer "+self.api_key,
            #这是我的api key，我有权调用这个接口
            "Content-Type":"application/json"
            #我接下来发给你的请求内容是json格式
        }
        data = {
        "model": self.model_name,
        "messages": messages
        }
        response = requests.post(
        self.base_url,
        #用post：向服务器提交模型+message
        #发到哪里
        headers=headers,
        #身份验证，数据格式
        json=data,
        #   真正发给模型的请求内容，本来data是dict，requests把序列化成json，再发给服务器
        timeout=30
        )
                        
        #   response.post 返回的是http response对象
       
        response.raise_for_status()
        #如果http状态码表示失败，就立刻抛异常
        result=response.json()
        return result["choices"][0]["message"]["content"]
