import requests
from tqdm import tqdm
url = 'https://www.pagalworld.com.sb/siteuploads/files/sfd143/71251/Dekha%20Tenu%20Pehli%20Pehli%20Baar%20Ve(PagalWorld.com.sb).mp3'
r = requests.get(url, stream= True)
TotalExpectBytes = int(r.headers["content-length"])
progress_bar = tqdm(total=TotalExpectBytes,unit='iB' ,unit_scale=True)
bytesRecieved = 0
with open('song.mp3', 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        # print(f"{TotalExpectBytes} recieved out of {bytesRecieved}" )
        f.write(chunk)
        progress_bar.update(128)
        bytesRecieved += 128
progress_bar.close()