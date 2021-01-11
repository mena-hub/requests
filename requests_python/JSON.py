import requests
import json

if __name__ == '__main__':
    url = "https://httpbin.org/get"
    args = {'limit': '10', 'offset': '20'}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        print(response.reason)
        print(response.url)
        # response_json = response.json()
        # origin = response_json['Origin']
        # print(origin)
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
    else:
        print(response, response.reason)