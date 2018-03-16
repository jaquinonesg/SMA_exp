import requests

r = requests.get('https://api.github.com/events')
if r.status_code == 200:
    print("rico")
print(r)