import requests

response = requests.get("https://api.github.com")
print(response.json())

#Название библиотеки: requests
#Для чего она используется: В этом случае код отправляет запрос на сервер https://api.github.com и возвращает его данные