import requests

payload = {"username": "joe", "password": "testing"}

#response = requests.get("https://httpbin.org/get", data=payload)
response = requests.post("https://httpbin.org/post", data=payload)

# print(response.text)

print(response.json())

# print(response)

dct =  response.json();

#print (dct['forms'])
