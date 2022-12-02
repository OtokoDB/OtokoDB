import requests
import os
import re
import json
import string
from bs4 import BeautifulSoup
f_trial = open("fanza-2-trial.txt", "w+")
parent_dir = os.getcwd()
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
        item_title = item_soup.find_all("h1")[0].text.strip("\n")
        item_preview = []
        item_otherlist = []
        item_tag = []
        item_tag.append("R18")
        item_tag.append("素人")
        item_trial_status = False
        intro_notice = False
        introduction = ""
        cover = item_soup.find_all("div", id="sample-video")[0]
        item_cover = cover.find_all("img")[0]["src"]
        previews = item_soup.find_all("a", {"name": "sample-image"})
        for preview in previews:
            preview_img = preview.find_all("img")[0]["src"]
            item_preview.append(preview_img.replace("js", "jp"))
        onclick_url = item_soup.find_all("a", class_="d-btn")
        if onclick_url != []:
            if "vrsample" in onclick_url[0]["onclick"]:
                item_onclick = "https://www.dmm.co.jp" + \
                    onclick_url[0]["onclick"][14:-16]
                pv_page = s.get(item_onclick)
                pv_soup = BeautifulSoup(pv_page.content, "html.parser")
                trial_target = pv_soup.find_all("script")[-2].text
                finder = re.findall(r'sampleUrl = .*;', trial_target)
                if finder == []:
                    trial_target = pv_soup.find_all("script")[-1].text
                    finder = re.findall(r'sampleUrl = .*;', trial_target)
                trial_url = "https:" + finder[0][13:-2]
                item_trial_status = True
            else:
                item_onclick = "https://www.dmm.co.jp" + \
                    onclick_url[0]["onclick"][12:-18]
                pv_page = s.get(item_onclick)
                pv_soup = BeautifulSoup(pv_page.text, "html.parser")
                pv_url = pv_soup.find_all(
                    "iframe", id="DMMSample_player_now")[0]["src"]
                pv2_page = s.get(pv_url)
                pv2_soup = BeautifulSoup(pv2_page.content, "html.parser")
                trial_target = pv2_soup.find_all("script")[-4].text[132:-10]
                jsonData = json.loads(trial_target)
                trial_url = "https:" + jsonData["src"]
                item_trial_status = True
            f_trial.write(trial_url+"\n")
        item_setups = item_soup.find_all("td", class_="nw")
        for item_setup in item_setups:
            if item_setup.text == "配信開始日：":
                item_date = item_setup.parent.find_all("td")[1].text.strip(
                    "\n").replace("/", "-") + " 12:00:00"
            elif item_setup.text == "収録時間：":
                item_size = item_setup.parent.find_all(
                    "td")[1].text.strip("\n")
            elif item_setup.text == "名前：":
                item_guest = item_setup.parent.find_all("td")[1].text.strip(
                    "\n")
            elif item_setup.text == "サイズ：":
                attrstr = "サイズ：" + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "レーベル：":
                attrstr = "レーベル：" + \
                    item_setup.parent.find_all("td")[1].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "ジャンル：":
                tags = item_setup.parent.find_all("td")[1].find_all("a")
                for tag in tags:
                    item_tag.append(tag.text)
            elif item_setup.text == "品番：":
                item_id = item_setup.parent.find_all("td")[1].text.strip("\n")
                item_cate = item_id.rstrip(string.digits)
        intro_block = item_soup.find_all("div", class_="mg-b20 lh4")[0]
        introduction_list = intro_block.findAll(text=True, recursive=False)
        for i in introduction_list:
            if i == "\n" or i == "\n\u3000":
                continue
            if i == " 特集 ":
                break
            introduction = introduction + i.strip("\n") + "\n"
        if intro_block.find_all("a") != []:
            intro_notice = True
        pricetag = item_soup.find_all("dt", class_="col2")[0].text.replace(" ", "").strip("\n") + "  " + item_soup.find_all(
            "dd", class_="limit")[0].text.replace(" ", "").strip("\n") + "  " + item_soup.find_all("dd", class_="price")[0].text.replace(" ", "").strip("\n")
        directory = "fanza/" + item_cate
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, exist_ok=True)
        f = open("fanza/" + item_cate + "/" + item_id + ".md", "w+")
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
        f.write("  - [Fanza, "+item_guest+"]\n")
        f.write("---"+"\n\n")
        for other in item_otherlist:
            f.write(other+"\n")
        f.write(pricetag+"\n\n")
        f.write("<!-- more -->"+"\n\n")
        f.write("## Preview"+"\n\n")
        f.write("![]("+item_cover+")\n\n")
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
        if item_trial_status == True:
            f.write("Trial download: "+trial_url+"\n")
            f.write(
                "{ % video https://drive.otoko.eu.org/api/raw/?path=/Trial/DLGetchu %}"+"\n\n")
        f.write("## Introduction"+"\n\n")
        f.write(introduction+"\n")
        if intro_notice == True:
            f.write("Please note that this intro has links, check it!"+"\n\n")
        f.write("## Download"+"\n\n")
        f.write(
            '''<div class="text-center">{% btn #, '''+item_size+" , fa fa-link %}</div>"+"\n")
        f.close()
        print("Markdown file generated for item: "+item_id)
f_trial.close()
print("Task completed.")
