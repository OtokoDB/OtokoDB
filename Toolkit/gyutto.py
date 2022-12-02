import requests
import math
import os
from bs4 import BeautifulSoup
parent_dir = os.getcwd()
s = requests.Session()
pagenum = 1
f_trial=open("gyutto-trial.txt","w+")
status = True
while status == True:
    url = "http://gyutto.com/search/search_list.php?genre_id=20738&category_id=10&set_category_flag=1&pageID=" + \
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
        item_title = item_soup.find_all("h1")[0].text.strip("\n")
        trial_status = False
        trial_check_page = s.get("http://gyutto.com/item/item_sample.php?id="+item_id)
        if trial_check_page.text != "":
            trial_check_soup = BeautifulSoup(trial_check_page.text,"html.parser")
            if  trial_check_soup.find_all("a")[0]["href"] == "#":
                trial_url = trial_check_soup.find_all("a")[0]["onclick"][9:-15].split(",")[0].replace('\'','')
            else:
                trial_url = trial_check_soup.find_all("a")[0]["href"]
            f_trial.write(trial_url+"\n")
            trial_status = True
        cover_list = item_soup.find_all("div", class_="ItemPh")
        item_tag = []
        more_info = item_soup.find_all("div", class_="unit_DetailMoreInfo")[0].find_all("dl")[0].find_all("dd")[0].text
        if "全年齢" in more_info:
            item_tag.append("Normal")
        elif "15禁" in more_info:
            item_tag.append("R15")
        elif "18禁" in more_info:
            item_tag.append("R18")
        preview_list = []
        for x in cover_list:
            x_url = x.find_all("img")[0]["src"]
            preview_list.append("http://gyutto.com"+x_url)
        item_append_list = []
        detail_lead = item_soup.find_all("div",class_="unit_DetailLead")[0].find_all("p")[0].text
        item_append_list.append(detail_lead)
        item_table = item_soup.find_all("div",id="noMovie")[0].find_all("div",class_="unit_DetailBasicInfo")[0].find_all("dl", class_="BasicInfo clearfix")
        for x in item_table:
            if x.find_all("dt")[0].text == "カテゴリー":
                item_tag.append(x.find_all("dd")[0].text)
            elif x.find_all("dt")[0].text == "サークル":
                item_cate = x.find_all("dd")[0].find_all("a")[0].text
                item_cate_id = x.find_all("dd")[0].find_all("a")[0]["href"][63:67].strip("&")
            elif x.find_all("dt")[0].text == "ジャンル":
                taglist = x.find_all("dd")[0].find_all("a")
                for y in taglist:
                    item_tag.append(y.text)
            elif x.find_all("dt")[0].text == "配信開始日":
                item_date = x.find_all("dd")[0].text.replace(
                    "年", "-").replace("月", "-").replace("日", "") + " 12:00:00"
            elif x.find_all("dt")[0].text == "ページ数":
                attrstr = "ページ数: "+x.find_all("dd")[0].text
                item_append_list.append(attrstr)
            elif x.find_all("dt")[0].text == "ボイス":
                attrstr = "ボイス: "+x.find_all("dd")[0].text
                item_append_list.append(attrstr)
            elif x.find_all("dt")[0].text == "再生時間":
                attrstr = "再生時間: "+x.find_all("dd")[0].text
                item_append_list.append(attrstr)
        intro_list = []
        detail_list = item_soup.find_all("div", class_="unit_DetailSummary clearfix")
        for x in detail_list:
            try:
                attr = x.find_all("p")[0].text
                intro_list.append(attr)
            except IndexError:
                intro_list.append("Special Intro detected!")
        price_url = "https://gyutto.com/item/item_buy.php?id="+item_id
        price_page = s.get(price_url)
        price_soup = BeautifulSoup(price_page.text,"html.parser")
        if price_soup.find_all("p",class_="DefiPrice") == []:
            pricetag = ""
        else:
            pricetag = price_soup.find_all("p",class_="DefiPrice")[0].text
        directory = "gyutto/"+item_cate_id
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, exist_ok=True)
        f = open("gyutto/"+item_cate_id+"/"+item_id+".md", "w+")
        if len(preview_list) == 1:
            md_gp = ""
            md_endgp = ""
        elif len(preview_list) == 2 or len(preview_list) == 4 or len(preview_list) == 7:
            md_gp = "{% gp "+str(len(preview_list))+"-1 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        elif len(preview_list) <= 10 and len(preview_list) > 1:
            md_gp = "{% gp "+str(len(preview_list))+"-2 %}"+"\n"
            md_endgp = "{% endgp %}"+"\n"
        f.write("---"+"\n")
        f.write("title: "+item_title+"\n")
        f.write("date: "+item_date+"\n")
        f.write("tags:"+"\n")
        for tag in item_tag:
            f.write("  - "+tag+"\n")
        f.write("categories:"+"\n")
        f.write("  - [Gyutto, "+item_cate+"]"+"\n")
        f.write("---"+"\n\n")
        for other in item_append_list:
            f.write(other+"\n")
        if pricetag != "":
            f.write(pricetag+"\n\n")
        f.write("<!-- more -->"+"\n\n")
        f.write("## Preview"+"\n\n")
        f.write(md_gp)
        for cover in preview_list:
            f.write("![]("+cover+")\n")
        f.write(md_endgp+"\n")
        if trial_status == True:
            f.write("Trial download: "+trial_url+"\n")
            f.write(
                "{ % video https://drive.otoko.eu.org/api/raw/?path=/Trial/DLGetchu %}"+"\n\n")
        f.write("## Introduction"+"\n\n")
        for x in intro_list:
            f.write(x+"\n\n")
        f.write("## Download"+"\n\n")
        f.write(
            '''<div class="text-center">{% btn #, Download , fa fa-link %}</div>'''+"\n")
        f.close()
        print("Markdown file generated for item: "+item_id)
    pagenum += 1
    if pagenum > page_max:
        break
print("Task completed.")
f_trial.close()