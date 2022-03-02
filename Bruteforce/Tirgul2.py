import requests
from bs4 import BeautifulSoup
URL = "https://linoit.com/session/login?dispLang=en_US"
username = "mekifh"
password = "mahalkita"
site_content = requests.post(URL, data={"username": username, "password":password})
soup = BeautifulSoup(site_content.content, 'html.parser')
count = 0
count1 = 0
count2 = 0
for href in soup.find_all(href=""):
    if href.text == "CyberClass" and count<1:
        print(href.text)
        count+=1
    if href.text == "Hila" and count1<1:
        print(href.text)
        count1+=1
    if href.text == "Main" and count2<1:
        print(href.text)
        count2+=1