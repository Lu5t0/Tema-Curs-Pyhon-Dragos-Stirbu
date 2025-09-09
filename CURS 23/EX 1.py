import requests

if __name__ == '__main__':
    r = requests.get('http://httpbin.org/get')
    print(r.status_code)
    print(r.text[:200])
