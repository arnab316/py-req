import requests
playload = {'postId':'3'}
r= requests.get('https://jsonplaceholder.typicode.com/comments', params=playload)
# print(r.url)
print(r.text)
