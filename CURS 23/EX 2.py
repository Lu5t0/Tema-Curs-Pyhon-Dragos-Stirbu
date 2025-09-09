import requests

if __name__ == '__main__':
    parametri = {"nume": "Ion", "varsta": 25
    }
    response = requests.get("https://httpbin.org/get", params=parametri)
    print(response.json())