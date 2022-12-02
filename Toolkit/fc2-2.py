import requests
import math
import os
from bs4 import BeautifulSoup
parent_dir = os.getcwd()
s = requests.Session()
f_trial = open("fc2-2-trial.txt","w+")
pagenum = 1
status = True
while status == True:
    url = "https://adult.contents.fc2.com/search/?tag=%E5%A5%B3%E8%A3%85&page=" + \
        str(pagenum)
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    itemcount = soup.find_all("div", class_="search_header")[
        0].find_all("p")[0].text[-4:-1]
    page_max = math.ceil(int(itemcount)/30)
    print("Processing page: " + str(pagenum) + " of " + str(page_max))
    item_urls = soup.find_all("a", class_="c-cntCard-110-f_thumb_link")
    for item_url in item_urls:
        if "?tag" in item_url["href"] or "users" in item_url["href"] :
            continue
        print("Processing item: "+item_url["href"][9:-1])
        item_id = item_url["href"][9:-1]
        if item_url.parent.find_all("iframe") != []:
            item_pv_iframe = "https://adult.contents.fc2.com" + item_url.parent.find_all("iframe")[0]["data-player-src"]
            f_trial.write(item_pv_iframe+"\n")
        else:
            item_pv_iframe = ""
        item_page = s.get("https://adult.contents.fc2.com" + item_url["href"])
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_title = item_soup.find_all("h3")[0].text.strip("\n")
        item_preview = []
        item_tag = []
        item_tag.append("R18")
        item_trial_status = False
        intro_notice = False
        introduction = ""
        cover_area = item_soup.find_all("div",class_="items_article_MainitemThumb")[0]
        cover = "https:/"+cover_area.find_all("img")[0]["src"][34:]
        item_size = cover_area.find_all("p")[0].text
        item_header = item_soup.find_all("div", class_="items_article_headerInfo")[0]
        item_cate = item_header.find_all("ul")[0].find_all("li")[-1].find_all("a")[0].text
        item_cate_id = item_header.find_all("ul")[0].find_all("li")[-1].find_all("a")[0]["href"][37:-1]
        if "author_id" in item_cate_id:
            item_cate_id = item_header.find_all("ul")[0].find_all("li")[-1].find_all("a")[0]["href"][49:]
        tag_area = item_soup.find_all("a", class_="tag tagTag")
        for i in tag_area:
            tag = i["data-tag"]
            item_tag.append(tag)
        item_date = item_soup.find_all("div", class_="items_article_Releasedate")[0].text[6:].strip(
                    "\n").replace("/", "-") + " 12:00:00"
        previews = item_soup.find_all("a", {"data-image-slideshow": "sample-images"})
        for preview in previews:
            preview_img = preview["href"]
            item_preview.append(preview_img)
        pricetag = item_soup.find_all("section", class_="items_article_mylistBox")[0]
        pricing = pricetag.find_all("h3")[0].text + "  " + pricetag.find_all("p")[0].text
        directory = "fc2/" + item_cate_id
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, exist_ok=True)
        f = open("fc2/" + item_cate_id + "/" + item_id + ".md", "w+")
        if len(item_preview) == 1:
            md_gp = ""
            md_endgp = ""
        elif len(item_preview) == 2 or len(item_preview) == 4 or len(item_preview) == 7:
            md_gp = "{% gp "+str(len(item_preview))+"-1 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        elif len(item_preview) <= 10 and len(item_preview) > 1:
            md_gp = "{% gp "+str(len(item_preview))+"-2 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        elif len(item_preview) == 11:
            md_gp = "{% gp 10-2 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        elif len(item_preview) > 11:
            md_gp = "{% gp "+str(len(item_preview)-10)+"-2 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        f.write("---"+"\n")
        f.write("title: "+item_title+"\n")
        f.write("date: "+item_date+"\n")
        f.write("tags:"+"\n")
        for tag in item_tag:
            f.write("  - "+tag+"\n")
        f.write("categories:"+"\n")
        f.write("  - [FC2, "+item_cate+"]\n")
        f.write("---"+"\n\n")
        f.write(pricing+"\n\n")
        f.write("<!-- more -->"+"\n\n")
        f.write("## Preview"+"\n\n")
        f.write("![]("+cover+")\n\n")
        if len(item_preview) <= 10 and len(item_preview) > 0:
            f.write(md_gp)
            for preview in item_preview:
                f.write("![]("+preview+")\n")
            f.write(md_endgp+"\n")
        elif len(item_preview) == 11:
            f.write(md_gp)
            for preview in item_preview[0:10]:
                f.write("![]("+preview+")\n")
            f.write(md_endgp+"\n")
            f.write("![]("+item_preview[10]+")\n\n")
        elif len(item_preview) > 11:
            f.write("{% gp 10-2 %}"+"\n")
            for preview in item_preview[0:10]:
                f.write("![]("+preview+")\n")
            f.write(md_endgp+"\n")
            f.write(md_gp)
            for preview in item_preview[10:]:
                f.write("![]("+preview+")\n")
            f.write(md_endgp+"\n")
        if item_pv_iframe != "":
            f.write("Trial download: "+item_pv_iframe+"\n")
            f.write(
            "{ % video https://drive.otoko.eu.org/api/raw/?path=/Trial/DLGetchu %}"+"\n\n")
        f.write("## Introduction"+"\n\n")
        f.write("Please note that this intro has links, check it!"+"\n\n")
        f.write("## Download"+"\n\n")
        f.write(
            '''<div class="text-center">{% btn #, '''+item_size+" , fa fa-link %}</div>"+"\n")
        f.close()
        print("Markdown file generated for item: "+item_id)
    pagenum += 1
    if pagenum > page_max:
        break
f_trial.close()
print("Task completed.")
