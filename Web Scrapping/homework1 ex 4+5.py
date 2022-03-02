#ex 4
import requests
from bs4 import BeautifulSoup

URL = "https://keithgalli.github.io/web-scraping/webpage.html"
content = requests.get(URL).text
soup = BeautifulSoup(content, 'html.parser')
print(soup.find_all(class_="regular gp")[2].text.replace(" ",""))
print(soup.find_all(class_="season sorted")[2].text.replace(" ",""))
print(soup.find(href="https://www.eliteprospects.com/team/10263/mit-mass.-inst.-of-tech./2018-2019?tab=stats").text.replace(" ",""))
print(soup.find_all('h2')[5].text.replace(" ",""))

#ex 5
URL = "https://www.ivory.co.il/catalog.php?id=18948"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64;  x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.content, 'html.parser')
title = soup.find('title').text
price = soup.find(class_="print-no-eilat-price").text
print(f"product's name: {title}\nproduct's price: {price}")