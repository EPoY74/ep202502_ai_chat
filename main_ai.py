"""
Трогаю лапкой работу с OpenAI лапкой
Автор: Евгений Петров
epoy74@gmail.com
+7 952 517 4228
"""

from openai import OpenAI

import settings_sec

sec_api_key=settings_sec.API_KEY
sec_base_url=settings_sec.BASE_URL
model_ai = "deefseek-chat"

if __name__ == "__main__":
    question:str = input("Свой вопрос: ") 
    client = OpenAI(api_key = sec_api_key, base_url=sec_base_url)
    while(question != "exit"):
        responce = client.chat.completions.create(
            model=model_ai,
            messages=[
                {"role":"system", "content":"Ты ученый, читающий лекцию студентам"},
                {"role":"user", "content":question},
            ]
        )
        question = input("Введи свой вопрос(exit для выхода): ")