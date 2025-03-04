import json
import requests
from pprint import pprint

base_url = "https://httpbin.org/post"

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,uk;q=0.7",
    "Host": "httpbin.org",
    "Priority": "u=1, i",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-67c4a4a8-6b175bdc7843ed7b44b040c4"
}

payload = {
    "custname": "Ivan",
    "custtel": "81234568",
    "custemail": "ivan@gmail.com",
    "size": "small",
    "topping": "onion",
    "delivery": "20:45",
    "comments": "dasdfas"
}

try:
    response = requests.post(base_url, headers=headers, data=payload)
    # print(response.status_code)
    pprint(response.json())
    # print()
    # print(response.headers)
    # print()
    # pprint(json.loads(response.content)['json'])
except requests.exceptions.RequestException as e:
    print(e)
