import requests
import math
import os
from bs4 import BeautifulSoup
parent_dir = os.getcwd()
f_trial = open("dlgetchu-trial.txt", "w+")
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
        item_urls = item.find_all("a")
        item_id = item_urls[0]["href"][28:]
        item_title = item_urls[0].text
        item_circle = item_urls[1].text
        item_br = item.find_all("br")
        item_search_intro = item_br[-4].next_sibling.strip()
        print("Processing item: "+item_id)
        item_page = s.get(item_urls[0]["href"])
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_circle_id = item_soup.find_all(
            "td", class_="font10")[0].text[-7:-1]
        item_centers = item_soup.find_all("td", {"align": "center"})
        item_keys = item_soup.find_all("td", class_="item-key")
        item_setups = item_soup.find_all("td", class_="bluetext")
        item_price = item_soup.find_all("div", class_="cart_new_C2")[0].text
        item_cover = []
        item_taglist = []
        item_otherlist = []
        item_trial_status = False
        trial_url = ""
        for item_center in item_centers:
            item_img = item_center.find_all("img")
            if item_img == []:
                continue
            if "item_img" in item_img[0]["src"]:
                item_cover.append("https://dl.getchu.com"+item_img[0]["src"])
        for item_center in item_centers:
            if item_center.find_all("a") == []:
                continue
            if "sample" in item_center.find_all("a")[0]["href"]:
                item_trial_status = True
                trial_url = item_center.find_all("a")[0]["href"]
                f_trial.write(trial_url + "\n")
                break
        for item_setup in item_setups:
            if item_setup.text == "作品内容":
                item_introduction = item_setup.parent.find_all("td")[1].text
            elif item_setup.text == "配信開始日":
                item_date = item_setup.parent.find_all("td")[1].text.strip(
                    "\n").replace("/", "-") + " 12:00:00"
            elif item_setup.text == "画像数&ページ数":
                item_size_1 = item_setup.parent.find_all(
                    "td")[1].text.strip("\n")
            elif item_setup.text == "ダウンロード容量":
                item_size_2 = item_setup.parent.find_all(
                    "td")[1].text.strip("\n")
            elif item_setup.text == "作者":
                attrstr = "作者: " + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "特記事項":
                attrstr = "特記事項: " + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "カテゴリ":
                attrstr = "カテゴリ: " + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "プロテクトの有無":
                attrstr = "プロテクトの有無: " + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "バージョン":
                attrstr = "バージョン: " + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "オフィシャルＨＰ":
                attrstr = "オフィシャルＨＰ: " + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "指定年齢":
                age_tag = item_setup.parent.find_all("img")[0]["src"]
                if age_tag == "/images/ai_age_18.gif":
                    item_taglist.append("R18")
                elif age_tag == "/images/ai_age_ippan.gif":
                    item_taglist.append("Normal")
                elif age_tag == "/images/ai_age_r.gif":
                    item_taglist.append("R15")
        for item_key in item_keys:
            item_tags = item_key.find_all("a")
            for item_tag in item_tags:
                item_taglist.append(item_tag.text)
        if item_size_1 != "" and item_size_2 != "":
            item_size = item_size_1 + " / " + item_size_2
        elif item_size_1 == "" and item_size_2 == "":
            item_size = ""
        else:
            item_size = item_size_1 + item_size_2
        directory = "dlgetchu/"+item_circle_id
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, exist_ok=True)
        f = open("dlgetchu/"+item_circle_id+"/"+item_id+".md", "w+")
        if len(item_cover) == 1:
            md_gp = ""
            md_endgp = ""
        elif len(item_cover) == 2:
            md_gp = "{% gp 2-2 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        elif len(item_cover) == 3:
            md_gp = "{% gp 3-1 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        else:
            md_gp = "{% gp 4-2 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        f.write("---"+"\n")
        f.write("title: "+item_title+"\n")
        f.write("date: "+item_date+"\n")
        f.write("tags:"+"\n")
        for tag in item_taglist:
            f.write("  - "+tag+"\n")
        f.write("categories:"+"\n")
        f.write("  - [DLGetchu, "+item_circle+"]"+"\n")
        f.write("---"+"\n\n")
        f.write(item_search_intro+"\n")
        for other in item_otherlist:
            f.write(other+"\n")
        f.write(item_price+"\n\n")
        f.write("<!-- more -->"+"\n\n")
        f.write("## Preview"+"\n\n")
        f.write(md_gp)
        for cover in item_cover:
            f.write("![]("+cover+")\n")
        f.write(md_endgp+"\n")
        if item_trial_status == True:
            f.write("Trial download: "+trial_url+"\n")
            f.write(
                "{ % video https://drive.otoko.eu.org/api/raw/?path=/Trial/DLGetchu %}"+"\n\n")
        f.write("## Introduction"+"\n\n")
        f.write(item_introduction+"\n\n")
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
