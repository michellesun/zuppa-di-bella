import requests

github = requests.get('https://github.com/timeline.json')

print github.text

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get("http://httpbin.org/get", params=payload)

print r.url