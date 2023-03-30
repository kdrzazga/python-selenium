import requests # pip install requests is pre-required

base_url = 'http://localhost:8081'
resp = requests.get(base_url)
data = resp.text

print(data)
