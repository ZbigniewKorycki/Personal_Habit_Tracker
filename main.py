import requests
from datetime import datetime
import config

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = config.TOKEN
USERNAME = config.USERNAME


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {"X-USER-TOKEN": TOKEN}

GRAPH = "graph1"

graph_config = {
    "id": GRAPH,
    "name": "Programming Graph",
    "unit": "min",
    "type": "float",
    "color": "sora",
}

post_record = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")

post_config = {
    "date": DATE,
    "quantity": input("How many minutes you learn programming today?\n")
}

response = requests.post(url=post_record, json=post_config, headers=headers)
print(response.text)
