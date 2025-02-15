"""
Трогаю лапкой работу с OpenAI лапкой
Автор: Евгений Петров
epoy74@gmail.com
+7 952 517 4228
"""

import sys
import traceback
from openai import(OpenAI,
                   APIStatusError)

import settings_sec

sec_api_key=settings_sec.API_KEY
sec_base_url=settings_sec.BASE_URL
model_ai = "deefseek-chat"

if __name__ == "__main__":
    question:str = input("Введи свой вопрос: ") 
    client = OpenAI(api_key = sec_api_key, base_url=sec_base_url)
    while(question != "exit"):
        try:
            responce = client.chat.completions.create(
                model=model_ai,
                messages=[
                    {"role":"system", "content":"Ты ученый, читающий лекцию студентам"},
                    {"role":"user", "content":question},
                ]
                
            )
            print(responce.choices[0].message.content)
            question = input("Введи свой вопрос(exit для выхода): ")
        except APIStatusError as err:
            err_responce = err.response.json()
            err_code = str(err.response.status_code)
            err_type_code:str = err_responce["error"]["code"]
            err_message:str = err_responce["error"]["message"]
            print("Код ошибки: ", err_code)
            print("Текстовый код ошибки: ", err_type_code)
            print("Текст ошибки: ",  err_message)
            sys.tracebacklimit = 0  # Прокидываю ошибку, без вывода стека на экран
            raise err
            exit(1)