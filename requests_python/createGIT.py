import requests
from pprint import pprint

if __name__ == '__main__':
    access_token = os.getenv("ACCESS_TOKEN")
    
    url = "https://api.github.com/gists"
    payload = {"public": False, "files": {"code.py": {"content": "print('To err is human, to purr feline.')"},}}
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f"token {access_token}"}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        pprint(response.json())
    else:
        print(response, response.reason)