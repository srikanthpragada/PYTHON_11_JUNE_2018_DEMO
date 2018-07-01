from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com/default.aspx")
soup = BeautifulSoup(resp.text, "html.parser")
for item in soup.find_all("a"):
    print(item.get_text())
    print(item["href"])