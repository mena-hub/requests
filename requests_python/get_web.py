import requests
from requests.exceptions import HTTPError

if __name__ == '__main__':
    url = "https://google.com"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as errh:
        print(f"HTTP error: {errh}")
    except Exception as err:
        print(f"Otro tipo de error: {err}")
    else:
        print(response.reason)
        print(response.content[:200])