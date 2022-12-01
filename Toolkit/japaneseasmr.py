import requests
from bs4 import BeautifulSoup

pagetarget = 5

f = open("asmr-url.txt", "w+")
s = requests.Session()
pagenum = 1
while pagenum <= pagetarget:
    print("Processing page: " + str(pagenum))
    url = "https://japaneseasmr.com/page/" + str(pagenum)
    page = s.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.find_all("h2", class_="entry-title")
    for item in items:
        item_url = item.find_all("a")[0]["href"]
        print("Processing item: " + item_url[25:-1])
        item_page = s.get(item_url)
        item_soup = BeautifulSoup(item_page.content, "html.parser")
        item_date = item_soup.find_all("time")[0]["datetime"]
        if item_date == "2022-11-20":
            break
        else:
            item_dls = item_soup.find_all("p", id="downloadlink")
        for item_dl in item_dls:
            item_dl_url = item_dl.find_all("a")[0]["href"]
            if "dla" in item_dl_url:
                continue
            else:
                f.write(item_dl_url + "\n")
    pagenum += 1
f.close()
print("Task completed.")
