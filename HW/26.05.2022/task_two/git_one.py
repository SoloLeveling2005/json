import requests
import json




url = "https://jsonplaceholder.typicode.com/comments?id=1"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)

with open("get_one.json", 'w') as file:
    json.dump(json_data, file)


















# get_one.json