import requests

respons = requests.get("https://jsonplaceholder.typicode.com/comments")

# print(respons.json())
jsonData = respons.json()
# print(jsonData[0])
# print(jsonData[0]['id'])

# for data in jsonData:
#     print(data)

# res = requests.post("https://jsonplaceholder.typicode.com/posts")
# print(res.json())

# param = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
param = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 1})
# print(param.json())

for Data in param.json():
    print(Data)