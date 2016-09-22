from bs4 import BeautifulSoup
import urllib.request

def crawl(url, title):
    page = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(page, 'html.parser')

    contents = soup.findAll("div", { "class" : "text" })
    for content in contents:
        with open(title, "a") as myfile:
            myfile.write(content.get_text())

for n in range(762166, 755000, -1):
    url = "http://www.hani.co.kr/arti/economy/economy_general/" + str(n) + ".html"
    crawl(url, "data/raw_hani_8_recent.txt")

for n in range(755000, 750000, -1):
    url = "http://www.hani.co.kr/arti/economy/economy_general/" + str(n) + ".html"
    crawl(url, "data/raw_hani_7_8.txt")




#url = "http://www.hani.co.kr/arti/society/society_general/761979.html"
#crawl(url)
