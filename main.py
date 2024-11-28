# 1
import requests

url = "https://api.github.com/search/repositories"
params = {
    "q": "html"
}

response = requests.get(url, params=params)

print(f"Статус-код ответа: {response.status_code}")
print(response.json())

# 2
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}
response = requests.get(url, params=params)

for post in response.json():
    print(post)

# 3

url = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, params)

print(f'responce code - f{response.status_code}')

for post in response.json():
    print(post)