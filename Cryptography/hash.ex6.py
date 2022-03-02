import requests
from bs4 import BeautifulSoup
import hashlib
with open('iview459_x64_setup.exe', 'rb') as afile:
    afile = afile.read()
hash = hashlib.sha256(afile)
print(hash.hexdigest())
URL = "https://www.irfanview.com/64bit.htm"
site = requests.get(URL)
soup = BeautifulSoup(site.text,"html.parser")
if f"(SHA-256 checksum: {hash.hexdigest()})" in soup.text:
    print("original file")
else:
    print("danger! fake file")