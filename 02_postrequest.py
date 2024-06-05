import requests

r = requests.post('https://httpbin.org/post', data={'test': 'success'})
print(r.text)