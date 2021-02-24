import requests
from datetime import datetime


USERNAME = "fredericogago"
TOKEN = ""
GRAPH_ID = "frederico1"

pixela_endpoint = "https://pixe.la/v1/users"

create_account_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create your user account:
# response = requests.post(url=pixela_endpoint, json=create_account_params)

# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@fredericogago , it is your profile page!","isSuccess":true}


# Create a graph definition:
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Code Hours",
    "unit": "minute",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}


# Post value to the graph
today = datetime.now()

value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60",
}

# response = requests.post(url=value_endpoint, json=value_params, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}


# Update a Pixel in Graph
yesterday = datetime(year=2021, month=2, day=23)
yesterday = yesterday.strftime("%Y%m%d")

update_endpoint = f"{value_endpoint}/{yesterday}"

update_params = {
    "quantity": "90",
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}


# Delete a Pixel in Graph

delete_endpoint = f"{value_endpoint}/{yesterday}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}
