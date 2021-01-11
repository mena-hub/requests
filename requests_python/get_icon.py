import requests 

if __name__ == '__main__':
    url = "https://www.google.com/favicon.ico"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.reason)
        file = open("downloads/get/google.ico", 'wb')
        file.write(response.content)
        file.close()
    elif response.status_code == 404:
        print(response.reason)