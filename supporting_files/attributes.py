import requests

response = requests.get("https://httpbin.org/")
attributes = [attname for attname in dir(response) if not attname.startswith("_")]
print(attributes)