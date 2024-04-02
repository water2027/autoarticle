import json
import openai

with open('config.json','r',encoding="utf-8") as f:
    config = json.load(f)
openai.api_key = config["api_key"]
openai.base_url = config["base_url"]

class AI:
    def __init__(self,role:str):
        self.role=role
        self.message=[{
            "role": "system",
            "content": config[role]
        }]

    def get_response(self,text:str):
        self.message.append({"role": "user", "content": text})
        wow=self.sendtoAI().choices[0].message
        self.message.append({"role": wow.role, "content": wow.content})
        print(self.message)
        return wow.content

    def sendtoAI(self):
        try:
            response = openai.chat.completions.create(
                model=config["model"],
                messages=self.message,
                max_tokens=128,
                temperature=1.0,
            )
            return response
        except Exception as e:
            print(e)
            return None
        