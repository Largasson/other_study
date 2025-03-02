import requests

base_url = "https://api.pachca.com/api/shared/v1"


headers = {
    "Authorization": "Bearer F79E6kLjBzyeeB4otztqtQkOtlqU7dFbHiakD24mJlc",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.pachca.com",
    "User-Agent": "Python-requests/2.x",
    "Connection": "close",
}

params = {
    # "per": "2",
    "query": "Петров"

}

try:
    response = requests.get(f"{base_url}/users", headers=headers, params=params)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)
