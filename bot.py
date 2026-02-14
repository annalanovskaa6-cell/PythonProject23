# import requests
# from config import Config, load_config
# config: Config = load_config()
# bot_token = config.bot.token
#GET - на получение данных сервера
#POST - отправляем данные на сервер или сохраняем
# response = requests.get("https://google.com")
# print(response.text)
#200 - ура
#404 500 412 - ошибки
# s = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
# print(s.text)
#JSON