import requests
from bs4 import BeautifulSoup

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    "url": "https://www.windguru.cz/49328",
    "ua": "local_renderscript",
    "waitTime": {"min": 10000, "max": 20000},
}

response = requests.post(
    "http://localhost:3000/render", headers=headers, json=json_data
)

soup = BeautifulSoup(response.json()["body"], "html.parser")
print(soup)
