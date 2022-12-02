import requests
import os
from bs4 import BeautifulSoup
parent_dir = os.getcwd()
s = requests.Session()
f_trial = open("dlsite-trial.txt", "w+")
url_list = ["https://www.dlsite.com/home/fsr/=/age_category%5B0%5D/general/work_category%5B0%5D/doujin/work_category%5B1%5D/pc/work_category%5B2%5D/app/order/release_d/work_type_category%5B0%5D/audio/genre%5B0%5D/303/genre%5B1%5D/111/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/from/left_pain.work_type", "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/pc/work_category%5B3%5D/app/order%5B0%5D/release_d/work_type_category%5B0%5D/audio/work_type_category_name%5B0%5D/%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%BBASMR/genre%5B0%5D/111/genre_name%5B0%5D/%E5%A5%B3%E8%A3%85/options_and_or/and/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/show_type/3/lang_options%5B0%5D/%E6%97%A5%E6%9C%AC%E8%AA%9E/lang_options%5B1%5D/%E8%8B%B1%E8%AA%9E/lang_options%5B2%5D/%E4%B8%AD%E5%9B%BD%E8%AA%9E/lang_options%5B3%5D/%E9%9F%93%E5%9B%BD%E8%AA%9E/lang_options%5B4%5D/%E8%A8%80%E8%AA%9E%E4%B8%8D%E8%A6%81/page/1", "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/pc/work_category%5B3%5D/app/order%5B0%5D/release_d/work_type_category%5B0%5D/audio/work_type_category_name%5B0%5D/%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%BBASMR/genre%5B0%5D/111/genre_name%5B0%5D/%E5%A5%B3%E8%A3%85/options_and_or/and/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/show_type/3/lang_options%5B0%5D/%E6%97%A5%E6%9C%AC%E8%AA%9E/lang_options%5B1%5D/%E8%8B%B1%E8%AA%9E/lang_options%5B2%5D/%E4%B8%AD%E5%9B%BD%E8%AA%9E/lang_options%5B3%5D/%E9%9F%93%E5%9B%BD%E8%AA%9E/lang_options%5B4%5D/%E8%A8%80%E8%AA%9E%E4%B8%8D%E8%A6%81/page/2",
            "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/pc/work_category%5B3%5D/app/order%5B0%5D/release_d/work_type_category%5B0%5D/audio/work_type_category_name%5B0%5D/%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%BBASMR/genre%5B0%5D/111/genre_name%5B0%5D/%E5%A5%B3%E8%A3%85/options_and_or/and/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/show_type/3/lang_options%5B0%5D/%E6%97%A5%E6%9C%AC%E8%AA%9E/lang_options%5B1%5D/%E8%8B%B1%E8%AA%9E/lang_options%5B2%5D/%E4%B8%AD%E5%9B%BD%E8%AA%9E/lang_options%5B3%5D/%E9%9F%93%E5%9B%BD%E8%AA%9E/lang_options%5B4%5D/%E8%A8%80%E8%AA%9E%E4%B8%8D%E8%A6%81/page/3", "https://www.dlsite.com/girls/fsr/=/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/drama/work_category%5B3%5D/pc/order/release_d/work_type_category%5B0%5D/audio/genre%5B0%5D/303/genre%5B1%5D/111/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/is_tl/1/is_bl/1/is_gay%5B0%5D/1/from/left_pain.work_type"]
for url in url_list:
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.find_all("dt", class_="search_img work_thumb")
    for item in items:
        item_url = item.find_all("a")[0]["href"]
        item_id = item_url[-13:-5]
        print("Processing item: "+item_id)
        item_page = s.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_title = item_soup.find_all("h1")[0].text.strip("\n")
        item_preview = []
        item_otherlist = []
        item_tag = []
        item_trial_status = False
        intro = []
        preview_data = item_soup.find_all(
            "div", class_="product-slider-data")[0].find_all("div")
        for preview in preview_data:
            preview_img = preview["data-src"]
            item_preview.append("https:"+preview_img)
        item_cate_place = item_soup.find_all("span", class_="maker_name")[
            0].find_all("a")[0]
        item_cate = item_cate_place.text
        item_cate_id = item_cate_place["href"][-12:-5]
        item_setups = item_soup.find_all("table", id="work_outline")[
            0].find_all("th")
        for item_setup in item_setups:
            if item_setup.text == "販売日":
                item_date = item_setup.parent.find_all("td")[0].text.replace(
                    "年", "-").replace("月", "-").replace("日", "") + " 12:00:00"
            elif item_setup.text == "年齢指定":
                age_tag = item_setup.parent.find_all("span")[0].text
                if age_tag == "18禁":
                    item_tag.append("R18")
                elif age_tag == "全年齢":
                    item_tag.append("Normal")
            elif item_setup.text == "ファイル容量":
                item_size = item_setup.parent.find_all(
                    "td")[0].text.replace(" ", "").strip("\n")
            elif item_setup.text == "声優":
                attrstr = "声優: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "更新情報":
                attrstr = "更新情報: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "作者":
                attrstr = "作者: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "イベント":
                attrstr = "イベント: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "イラスト":
                attrstr = "イラスト: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "シナリオ":
                attrstr = "シナリオ: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "シリーズ名":
                attrstr = "シリーズ名: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "その他":
                attrstr = "その他: " + \
                    item_setup.parent.find_all("td")[0].text.strip("\n")
                item_otherlist.append(attrstr)
            elif item_setup.text == "ジャンル":
                tags = item_setup.parent.find_all("td")[0].find_all("a")
                for tag in tags:
                    item_tag.append(tag.text)
        if item_soup.find_all("a", class_="btn_trial") != []:
            trial_url = "https:" + \
                item_soup.find_all("a", class_="btn_trial")[0]["href"]
            f_trial.write(trial_url + "\n")
            item_trial_status = True
            trial_size = item_soup.find_all("p", class_="trial_file")[0].parent.find_all(
                "span")[0].text.replace("(", "").replace(")", "")
        intro_block = item_soup.find_all(
            "div", class_="work_parts_container")[0]
        introlist = intro_block.find_all("div", recursive=False)
        for x in introlist:
            if x["class"][1] == "type_image":
                if x.find_all("h3") == []:
                    introduction = "![]("+x.find_all("a")[0]["href"] + \
                        ")\n\n"+x.find_all("p")[0].text+"\n\n"
                else:
                    introduction = "### "+x.find_all("h3")[0].text+"\n\n"+"![]("+x.find_all("a")[
                        0]["href"]+")\n\n"+x.find_all("p")[0].text+"\n\n"
                intro.append(introduction)
            elif x["class"][1] == "type_text":
                if x.find_all("h3") == []:
                    introduction = x.find_all("p")[0].text+"\n\n"
                else:
                    introduction = "### " + \
                        x.find_all("h3")[0].text+"\n\n" + \
                        x.find_all("p")[0].text+"\n\n"
                intro.append(introduction)
            else:
                continue
        pricetag = "価格: "+item_soup.find_all("div", id="work_buy_box_wrapper")[
            0].find_all("div")[0]["data-official_price"] + "円"
        directory = "dlsite/" + item_cate_id
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, exist_ok=True)
        f = open("dlsite/" + item_cate_id + "/" + item_id + ".md", "w+")
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
        f.write("  - [DLsite, "+item_cate+"]\n")
        f.write("---"+"\n\n")
        for other in item_otherlist:
            f.write(other+"\n")
        f.write(pricetag+"\n\n")
        f.write("<!-- more -->"+"\n\n")
        f.write("## Preview"+"\n\n")
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
                '''<div class="text-center">{% btn #, TrialFile/'''+trial_size+" , fa fa-link %}</div>"+"\n\n")
        f.write("## Introduction"+"\n\n")
        for x in intro:
            f.write(x)
        f.write("## Download"+"\n\n")
        f.write(
            '''<div class="text-center">{% btn #, '''+item_size+" , fa fa-link %}</div>"+"\n")
        f.close()
        print("Markdown file generated for item: "+item_id)
f_trial.close()
print("Task completed.")
