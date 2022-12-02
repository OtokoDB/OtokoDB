import requests
import math
from bs4 import BeautifulSoup
f = open("gyutto-2-category.txt","a+")
s = requests.Session()
pagenum = 1
status = True
while status == True:
    url = "http://gyutto.com/search/search_list.php?genre_id=19560&category_id=10&set_category_flag=1&pageID=" + \
        str(pagenum)
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    itemcount = soup.find_all("div", class_="RightBox")[
        0].text.strip("\n")[1:5]
    page_max = math.ceil(int(itemcount)/60)
    print("Processing page: " + str(pagenum) + " of " + str(page_max))
    items = soup.find_all("dd", class_="DefiPhotoName")
    for item in items:
        item_urls = item.find_all("a")
        item_id = item_urls[0]["href"][24:]
        print("Processing item: "+item_id)
        item_page = s.get(item_urls[0]["href"])
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_setups = item_soup.find_all("div",id="noMovie")[0].find_all("div",class_="unit_DetailBasicInfo")[0].find_all("dl", class_="BasicInfo clearfix")
        for item_setup in item_setups:
            f.write(item_setup.find_all("dt")[0].text + "\n")
    pagenum += 1
    if pagenum > page_max:
        break
print("Task completed.")
f.close()