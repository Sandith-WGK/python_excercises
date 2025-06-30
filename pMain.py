import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response)

content = response.json()

#print(content)

print("Total records: ",len(content))

import requests
print(requests.__version__)
