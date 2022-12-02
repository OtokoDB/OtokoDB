import requests
import math
import os
import json
from bs4 import BeautifulSoup
parent_dir = os.getcwd()
f_list = open("pornhub-list-date.txt","r+")
status = True
while status == True:
    item_id = f_list.readline().strip("\n")
    if item_id == "":
        break
    url = "https://jp.pornhub.com/view_video.php?viewkey=" + item_id
    print("Processing item: "+item_id)
    item_page = requests.get(url)
    item_soup = BeautifulSoup(item_page.text, "html.parser")
    item_circle_space = item_soup.find_all("div", class_="video-info-row userRow")[0]
    item_circle = item_circle_space.find_all("a")[0]["href"][7:]
    payload = item_soup.find_all(
        "script", type="application/ld+json")[0].text.strip("\n")
    loaded = json.loads(payload)
    item_title = loaded["name"]
    item_length = loaded["duration"].replace("PT", "").replace(
        "H", ":").replace("M", ":").replace("S", "")
    item_cover = loaded["thumbnailUrl"]
    item_upload = loaded["uploadDate"].replace(
        "+00:00", "").replace("T", " ")
    item_circle_name = loaded["author"]
    str_load = "| ["+item_id+"](https://drive.otoko.eu.org/Pornhub/"+item_circle+"/"+item_id+".mp4) | " + \
        item_title + " | " + item_length + " | " + \
        item_upload + " | ![](" + item_cover + ") |\n"
    directory = "pornhub/"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)
    try:
        fr = open("pornhub/"+item_circle+".md", "r+")
        fr.close()
    except FileNotFoundError:
        finit = open("pornhub/"+item_circle+".md", "w+")
        finit.write("---"+"\n")
        finit.write("title: "+item_circle_name+"\n")
        finit.write("date: "+item_upload+"\n")
        finit.write("tags:"+"\n")
        finit.write("  - R18"+"\n")
        finit.write("categories:"+"\n")
        finit.write("  - Pornhub\n")
        finit.write("---"+"\n\n")
        finit.write("## Introduction"+"\n\n")
        finit.write("## Download"+"\n\n")
        finit.write("{% button https://drive.otoko.eu.org/Pornhub/" +
            item_circle+"/, Download %}"+"\n\n")
        finit.write("<!-- more -->"+"\n\n")
        finit.write("## Videos"+"\n\n")
        finit.write("| ID | Title | Length | UploadTime | Cover |"+"\n")
        finit.write("| :----: | :----: | :----: | :----: | :----: |"+"\n")
        finit.close()
    fw = open("pornhub/"+item_circle+".md", "a+")
    fw.write(str_load)
    fw.close()
    print("Markdown file generated for item: "+item_id)
print("Task completed.")
f_list.close()
