import requests
import json

if __name__ == '__main__':
    url = "https://httpbin.org/post"
    payload = {'limit': '10', 'offset': '20'}
    headers = {'Content-Type': 'application/json', 'Authorization': 'token <access_token>'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print(response.reason)
        print(response.url)
        # print(response.content)
        response_headers = response.headers
        server = response_headers['Server']
        print(server)
    else:
        print(response, response.reason)