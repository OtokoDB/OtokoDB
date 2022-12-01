import requests
from bs4 import BeautifulSoup
import math
f = open("dlgetchu-category.txt", "w+")
s = requests.Session()
s.get("https://dl.getchu.com/adult_check.php?_adult_check=yes&url=gate%2F&ref_path=/")
pagenum = 1
status = True
while status == True:
    url = "https://dl.getchu.com/search/search_list.php?action=search&search_keyword=&perPage=50&search_age_flag=0&search_all_genre_id%5B3%5D%5B159%5D=30223&remove_search_keyword=&btnSearch=%B8%A1%BA%F7&dojin=1&pageID=" + \
        str(pagenum)
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    item_count = soup.find_all("td", {"height": "68"})[
        0].text.strip("件】の作品がみつかりました。\n").strip("【")
    page_max = math.ceil(int(item_count)/50)
    print("Processing page: " + str(pagenum) + " of " + str(page_max))
    items = soup.find_all("td", {"width": "430"})
    for item in items:
        item_url = item.find_all("a")[0]["href"]
        item_id = item_url[28:]
        print("Processing item: "+item_id)
        item_page = s.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_table = item_soup.find_all("td", class_="bluetext")
        for x in item_table:
            f.write(x.text+"\n")
    pagenum += 1
    if pagenum > page_max:
        break
f.close()
print("Task completed.")
