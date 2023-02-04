import requests

payload = {"page": 2, "count": 15}

response = requests.get("https://httpbin.org/get", params=payload)

print(response.url)
