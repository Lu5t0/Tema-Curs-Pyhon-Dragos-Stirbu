import requests

if __name__ == "__main__":
    response = requests.get("https://httpbin.org/status/404")

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Eroare:{response.status_code} pagina nu a fost gasita")

