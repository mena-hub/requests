import requests

if __name__ == '__main__':
    url = "https://httpbin.org/cookies"
    cookies = {'test_cookie': 'true'}
    response = requests.get(url, cookies=cookies)
    if response.ok:
        cookies = response.cookies
        print(cookies)
        print(response.content)