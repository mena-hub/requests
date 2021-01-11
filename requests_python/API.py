import requests

def get_stolenbikes (url="https://bikewise.org/api/v2/incidents", page=1):
    args = {'page': page, 'incident_type': 'theft', 'proximity': 'Chicago, IL', 'proximity_square': '50'} if page else {}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        payload = response.json()
        incidents = payload.get('incidents', [])
        if incidents:
            for stolenbike in incidents:
                title = stolenbike['title']
                address = stolenbike['address']
                print(f"\n title: {title} \n address: {address}")
        next = input("¿Continuar listado? [y/n]").lower()
        if next in ('y', 'yes'):
            get_stolenbikes(page=page+1)

if __name__ == '__main__':
    get_stolenbikes()