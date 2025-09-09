import requests

if __name__ == '__main__':
    response = requests.get("https://wttr.in/?format=j1")

    if response.status_code == 200:
        data = response.json()

    temperatura = data["current_condition"][0]["temp_C"]
    conditii = data["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"Temperata este de {temperatura} grade C si contia vremii este:{conditii}")


