import requests
from tqdm import tqdm
url = 'https://www.pagalworld.com.sb/siteuploads/files/sfd143/71229/O%20Sajni%20Re_320(PagalWorld.com.sb).mp3'

r = requests.get(url, stream=True)
TotalExpectBytes = int(r.headers["content-length"])

progress_bar = tqdm(total=TotalExpectBytes, unit='iB', unit_scale=True)

with open('song2.mp3', 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
     f.write(chunk)
     progress_bar.update(128)


progress_bar.close()
