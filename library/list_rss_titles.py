from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
soup = BeautifulSoup(resp.text, "xml") # must install lxml to use xml

for item in soup.find_all("item"):
    print(item.find("title").get_text())
    print(item.find("link").get_text())