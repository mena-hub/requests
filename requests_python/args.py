import requests

if __name__ == '__main__':
    url = "https://httpbin.org/get"
    args = {'limit': '10', 'offset': '20'}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        print(response.reason)
        print(response.url)
        print(response.content)
    else:
        print(response, response.reason)