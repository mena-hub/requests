import requests
import json

if __name__ == '__main__':
    url = "https://httpbin.org/post"
    payload = {'limit': '10', 'offset': '20'}
    # response = requests.post(url, json=payload)
    # response = requests.post(url, data=payload)
    response = requests.post(url, data=json.dumps(payload))

    if response.status_code == 200:
        print(response.reason)
        print(response.url)
        print(response.content)
    else:
        print(response, response.reason)