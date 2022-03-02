import threading
import requests
from bs4 import BeautifulSoup
import time
sites = ["https://www.ynet.co.il/home/0,7340,L-8,00.html","https://corona.mako.co.il/","https://13tv.co.il/","https://edition.cnn.com/","https://www.youtube.com/?gl=IL","https://www.calcalist.co.il/home/0,7340,L-8,00.html","https://www.one.co.il/","https://www.google.co.il/?hl=iw","https://www.maariv.co.il/news"]
def WriteSitesHTML(URL):
    file = open("SitesHTML.txt", "a")
    content = requests.get(URL)
    soup = BeautifulSoup(content.content, "html.parser")
    try:
        file.write(soup.prettify())
    except Exception:
        pass
    try:
        for title in soup.find('title'):  #soup.title
            print(title.get_text())
    except Exception:
        pass
    time.sleep(0.5)
start = time.perf_counter()
for URL in sites:
    # WriteSitesHTML(URL)    #without threading
    th1 = threading.Thread(target=WriteSitesHTML, args=(URL, ))
    th1.start()
th1.join()
stop = time.perf_counter()
print(f"Cycle time of all  : {stop-start}")
#Cycle time without threading: 7.8310675 sec
#Cycle time with threading: 1.1061386 sec
