import requests

response = requests.get("https://httpbin.org")
print(help(response))