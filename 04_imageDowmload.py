import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://images.unsplash.com/photo-1709828238515-35189879a02c?q=80&w=2072&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
i = Image.open(BytesIO(r.content))
f = open('img.jpeg', 'wb')
i.save(f)
f.close()