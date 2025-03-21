import requests

base_url = "https://api.pachca.com/api/shared/v1"

headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.pachca.com",
    "User-Agent": "Python-requests/2.x",
    "Connection": "close",
}

try:
    response = requests.get(f"{base_url}/users/{540901}", headers=headers)
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)
    