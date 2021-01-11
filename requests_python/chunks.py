import requests
import json

if __name__ == '__main__':
    url = "https://www.scoutmag.ph/wp-content/uploads/2020/08/dino-sword-chrome-dino.jpg"
    response = requests.get(url, stream=True)
    
    with open("downloads/chunks/image.jpg", 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    response.close()