import requests

if __name__ == '__main__':
    access_token = os.getenv("ACCESS_TOKEN")
    url = "https://api.github.com/user"

    session = requests.Session()
    session.headers.update({'Authorization': f"token {access_token}"})
    
    response = session.get(url)
    if response.ok:
        # print(response.content)
        response = session.get("https://github.com/mena-hub")
        if response.ok:
            print(response.cookies)
    else:
        print(response, response.reason)
        print(response.content)