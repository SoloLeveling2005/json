import requests
import json

i = 1
while True:
    url = "https://jsonplaceholder.typicode.com/comments?id=" + str(i)
    response = requests.get(url)
    json_data = response.content.decode()
    print(json_data)

    file_name = "json_files/get_one_" + str(i) + ".json"
    with open(file_name, 'w') as file:
        json.dump(json_data, file)

    if i == 30:
        break
    i += 1

















# get_one.json