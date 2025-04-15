# My progress of studying 100 days of code
import requests
import datetime as dt

USERNAME = "ianspangler"
TOKEN = "wqfhi3as7hdf756a3"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_paramas = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # CREATE NEW USER
# user_response = requests.post(url=pixela_endpoint, json=user_paramas)
# print(user_response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_paramas = {
    "id": ID,
    "name": "100daysofcode Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# # CREATE NEW GRAPH
# graph_response = requests.post(url=graph_endpoint, json=graph_paramas, headers=headers)
# print(graph_response.text)

post_value_endpoint = f"{graph_endpoint}/{ID}"

today = dt.datetime.now()

post_value_paramas = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study 100days of code today?"),
}

# # POST A NEW PIXEL
# post_value_response = requests.post(url=post_value_endpoint, json=post_value_paramas, headers=headers)
# print(post_value_response.text)

update_delete_endpoint = f"{post_value_endpoint}/{today.strftime("%Y%m%d")}"

update_paramas = {
    "quantity": "1"
}

# # UPDATE
# update_response = requests.put(url=update_delete_endpoint, json=update_paramas, headers=headers)
# print(update_response.text)

# # DELETE
# delete_response = requests.delete(url=update_delete_endpoint, headers=headers)
# print(delete_response.text)