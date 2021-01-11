import requests
from operator import itemgetter
from pprint import pprint

access_token = os.getenv("ACCESS_TOKEN")

if __name__ == '__main__':
    url = "https://api.github.com/repos/mena-hub/caffettiera_site/traffic/views"
    args = {'per': 'day',}
    headers = {'Authorization': f"token {access_token}"}
    response = requests.get(url, params=args, headers=headers)

    if response.status_code == 200:
        payload = response.json()
        print(f"El repositorio tiene {payload['count']} vistas y {payload['uniques']} únicos visitantes.")
        best_day = max(*list((day['count'], day['timestamp']) for day in payload['views']), key=itemgetter(0))
        pprint(payload)
        print(f"El repositorio obtuvo la mayoría de las vistas (total {best_day[0]}) el {best_day[1]}.")
    else:
        print(response, response.reason)

# Lambda
# best_day = max(*list((day['count'], day['timestamp']) for day in payload['views']), key=lambda x: x[0])