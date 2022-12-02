import requests
import math
import json
from bs4 import BeautifulSoup
pagenum = 1
status = True
listfile = open("pornhub-list.txt", "a+")
downloaded = []
while status == True:
    url = "https://jp.pornhub.com/video/search?search=%E7%94%B7%E3%81%AE%E5%A8%98&o=mr&page=" + \
        str(pagenum)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    itemcount = soup.find_all("div", class_="showingCounter")[
        0].text.replace(" ", "").strip("\n")[-9:-5]
    page_max = math.ceil(int(itemcount)/20)
    print("Processing page: " + str(pagenum) + " of " + str(page_max))
    items_box = soup.find_all("ul", id="videoSearchResult")[0]
    items = items_box.find_all("span", class_="title")
    for item in items:
        item_urls = item.find_all("a")
        item_url = "https://jp.pornhub.com"+item_urls[0]["href"]
        item_id = item_urls[0]["href"][24:]
        print("Processing item: "+item_id)
        if item_id in downloaded:
            continue
        else:
            downloaded.append(item_id)
        item_circle_url = item.parent.find_all("div", class_="usernameWrap")[
            0].find_all("a")[0]["href"]
        if "model" not in item_circle_url:
            continue
        elif "channel" in item_circle_url:
            continue
        item_circle = item_circle_url[7:]
        item_page = requests.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        payload = item_soup.find_all(
            "script", type="application/ld+json")[0].text.strip("\n")
        loaded = json.loads(payload)
        item_upload = loaded["uploadDate"].replace(
            "+00:00", "").replace("T", " ")
        listfile.write(item_id+","+item_upload+"\n")
        print("Markdown file generated for item: "+item_id)
    pagenum += 1
    if pagenum > page_max:
        break
pagenum = 1
while status == True:
    url = "https://jp.pornhub.com/video/search?search=%E5%A5%B3%E8%A3%85&o=mr&page=" + \
        str(pagenum)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    itemcount = soup.find_all("div", class_="showingCounter")[
        0].text.replace(" ", "").strip("\n")[-9:-5]
    page_max = math.ceil(int(itemcount)/20)
    print("Processing page: " + str(pagenum) + " of " + str(page_max))
    items_box = soup.find_all("ul", id="videoSearchResult")[0]
    items = items_box.find_all("span", class_="title")
    for item in items:
        item_urls = item.find_all("a")
        item_url = "https://jp.pornhub.com"+item_urls[0]["href"]
        item_id = item_urls[0]["href"][24:]
        print("Processing item: "+item_id)
        if item_id in downloaded:
            continue
        else:
            downloaded.append(item_id)
        item_circle_url = item.parent.find_all("div", class_="usernameWrap")[
            0].find_all("a")[0]["href"]
        if "model" not in item_circle_url:
            continue
        elif "channel" in item_circle_url:
            continue
        item_circle = item_circle_url[7:]
        item_page = requests.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        payload = item_soup.find_all(
            "script", type="application/ld+json")[0].text.strip("\n")
        loaded = json.loads(payload)
        item_upload = loaded["uploadDate"].replace(
            "+00:00", "").replace("T", " ")
        listfile.write(item_id+","+item_upload+"\n")
        print("Markdown file generated for item: "+item_id)
    pagenum += 1
    if pagenum > page_max:
        break
print("Task completed.")
listfile.close()
