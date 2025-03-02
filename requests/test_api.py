import requests
import json

# URL и заголовок авторизации
url = "https://api.pachca.com/api/shared/v1/users"
headers = {
    "Authorization": "Bearer F79E6kLjBzyeeB4otztqtQkOtlqU7dFbHiakD24mJlc",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Paw/3.1.10 (Macintosh; OS X/10.15.3) GCDHTTPRequest",
    "Connection": "close",
}

# Тело запроса
payload = {
    "user": {
        "first_name": "Олег122",
        "last_name": "Петров212",
        "email": "olegp342@example.com",
        "department": "Продукт",
        "list_tags": ["Product", "Design"],
        "custom_properties": [{"id": 1678, "value": "Санкт-Петербург"}],
    },
    "skip_email_notify": True,
}

# Выполнение POST-запроса
try:
    response = requests.post(url, headers=headers, data=payload)
    # Печать ответа
    print("Статус код:", response.status_code)
    print("Ответ:", response.json())
except requests.exceptions.RequestException as e:
    print(e)
