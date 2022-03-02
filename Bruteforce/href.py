from bs4 import BeautifulSoup
import requests
URL = 'https://keithgalli.github.io/web-scraping/webpage.html'
file_content = requests.get(URL)
soup = BeautifulSoup(file_content.content, 'html.parser')
for tag in soup.find_all(['a']):
    print(tag.get('href'))