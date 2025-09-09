import requests

if __name__ == "__main__":

    payload = {
        "utilizator": "admin",
        "parola": "1234"
    }
    response = requests.post("https://httpbin.org/post", json=payload)
    print(response.json())