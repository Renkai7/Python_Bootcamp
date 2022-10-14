import requests
import os
from datetime import datetime

USERNAME = "renkai7"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

# Create User
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Post value to graph
pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2022, month=10, day=13).strftime("%Y%m%d")

post_config = {
    "date": today,
    "quantity": "10",
}

# create_entry_response = requests.post(url=pixela_creation_endpoint, json=post_config, headers=headers)
# print(create_entry_response.text)

# Update value on graph
update_pixel_data = {
    "quantity": input("How many kilometers did you ride today? ")
}
pixela_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today}"
update_entry_response = requests.put(url=pixela_update_endpoint, json=update_pixel_data, headers=headers)
print(update_entry_response.text)

# Delete value in graph
# delete_entry_response = requests.delete(url=pixela_update_endpoint, headers=headers)
# print(delete_entry_response.text)