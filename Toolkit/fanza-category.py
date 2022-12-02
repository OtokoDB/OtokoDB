import requests
from bs4 import BeautifulSoup
import math
f = open("fanza-category.txt", "w+")
s = requests.Session()
s.get("https://www.dmm.co.jp/age_check/=/declared=yes/?rurl=https%3A%2F%2Fwww.dmm.co.jp%2Ftop%2F")
pagenum = 1
status = True
while status == True:
    url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=3036/sort=date/page=" + \
        str(pagenum)
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    itemcount = soup.find_all("div", class_="list-boxcaptside list-boxpagenation")[
        1].find_all("p")[0].text[0:4]
    page_max = math.ceil(int(itemcount)/120)
    print("Processing page: " + str(pagenum) + " of " + str(page_max))
    items = soup.find_all("p", class_="tmb")
    for item in items:
        item_url = item.find_all("a")[0]["href"]
        item_id = item_url.strip("?dmmref=keyword_3036&i3_ref=list&i3_ord=3")[52:-1]
        print("Processing item: "+item_id)
        item_page = s.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_setups = item_soup.find_all("td", class_="nw")
        for item_setup in item_setups:
            f.write(item_setup.text+"\n")
    pagenum += 1
    if pagenum > page_max:
        break
f.close()