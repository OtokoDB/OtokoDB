import requests
from bs4 import BeautifulSoup
import math
f = open("fanza-2-category.txt", "w+")
s = requests.Session()
s.get("https://www.dmm.co.jp/age_check/=/declared=yes/?rurl=https%3A%2F%2Fwww.dmm.co.jp%2Ftop%2F")
url_list = ["https://www.dmm.co.jp/digital/videoc/-/list/search/=/?searchstr=%E7%94%B7%E3%81%AE%E5%A8%98",
            "https://www.dmm.co.jp/digital/videoc/-/list/search/=/?searchstr=%E5%A5%B3%E8%A3%85"]
for url in url_list:
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.find_all("p", class_="tmb")
    for item in items:
        item_url = item.find_all("a")[0]["href"]
        item_id = item_url.strip("?i3_ref=search&i3_ord=1")[51:-1]
        print("Processing item: "+item_id)
        item_page = s.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_setups = item_soup.find_all("td", class_="nw")
        for item_setup in item_setups:
            f.write(item_setup.text+"\n")
f.close()
