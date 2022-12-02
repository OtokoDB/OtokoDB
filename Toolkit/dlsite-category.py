import requests
from bs4 import BeautifulSoup
f = open("dlsite-category.txt", "w+")
url_list = ["https://www.dlsite.com/home/fsr/=/age_category%5B0%5D/general/work_category%5B0%5D/doujin/work_category%5B1%5D/pc/work_category%5B2%5D/app/order/release_d/work_type_category%5B0%5D/audio/genre%5B0%5D/303/genre%5B1%5D/111/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/from/left_pain.work_type", "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/pc/work_category%5B3%5D/app/order%5B0%5D/release_d/work_type_category%5B0%5D/audio/work_type_category_name%5B0%5D/%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%BBASMR/genre%5B0%5D/111/genre_name%5B0%5D/%E5%A5%B3%E8%A3%85/options_and_or/and/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/show_type/3/lang_options%5B0%5D/%E6%97%A5%E6%9C%AC%E8%AA%9E/lang_options%5B1%5D/%E8%8B%B1%E8%AA%9E/lang_options%5B2%5D/%E4%B8%AD%E5%9B%BD%E8%AA%9E/lang_options%5B3%5D/%E9%9F%93%E5%9B%BD%E8%AA%9E/lang_options%5B4%5D/%E8%A8%80%E8%AA%9E%E4%B8%8D%E8%A6%81/page/1", "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/pc/work_category%5B3%5D/app/order%5B0%5D/release_d/work_type_category%5B0%5D/audio/work_type_category_name%5B0%5D/%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%BBASMR/genre%5B0%5D/111/genre_name%5B0%5D/%E5%A5%B3%E8%A3%85/options_and_or/and/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/show_type/3/lang_options%5B0%5D/%E6%97%A5%E6%9C%AC%E8%AA%9E/lang_options%5B1%5D/%E8%8B%B1%E8%AA%9E/lang_options%5B2%5D/%E4%B8%AD%E5%9B%BD%E8%AA%9E/lang_options%5B3%5D/%E9%9F%93%E5%9B%BD%E8%AA%9E/lang_options%5B4%5D/%E8%A8%80%E8%AA%9E%E4%B8%8D%E8%A6%81/page/2",
            "https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/pc/work_category%5B3%5D/app/order%5B0%5D/release_d/work_type_category%5B0%5D/audio/work_type_category_name%5B0%5D/%E3%83%9C%E3%82%A4%E3%82%B9%E3%83%BBASMR/genre%5B0%5D/111/genre_name%5B0%5D/%E5%A5%B3%E8%A3%85/options_and_or/and/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/show_type/3/lang_options%5B0%5D/%E6%97%A5%E6%9C%AC%E8%AA%9E/lang_options%5B1%5D/%E8%8B%B1%E8%AA%9E/lang_options%5B2%5D/%E4%B8%AD%E5%9B%BD%E8%AA%9E/lang_options%5B3%5D/%E9%9F%93%E5%9B%BD%E8%AA%9E/lang_options%5B4%5D/%E8%A8%80%E8%AA%9E%E4%B8%8D%E8%A6%81/page/3", "https://www.dlsite.com/girls/fsr/=/age_category%5B0%5D/general/age_category%5B1%5D/r15/age_category%5B2%5D/adult/work_category%5B0%5D/doujin/work_category%5B1%5D/books/work_category%5B2%5D/drama/work_category%5B3%5D/pc/order/release_d/work_type_category%5B0%5D/audio/genre%5B0%5D/303/genre%5B1%5D/111/options%5B0%5D/JPN/options%5B1%5D/ENG/options%5B2%5D/CHI/options%5B3%5D/KO_KR/options%5B4%5D/NM/per_page/100/is_tl/1/is_bl/1/is_gay%5B0%5D/1/from/left_pain.work_type"]
s = requests.Session()
for url in url_list:
    page = s.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.find_all("dt", class_="search_img work_thumb")
    for item in items:
        item_url = item.find_all("a")[0]["href"]
        print("Processing item: "+item_url[-13:-5])
        item_page = s.get(item_url)
        item_soup = BeautifulSoup(item_page.text, "html.parser")
        item_table = item_soup.find_all("table", id="work_outline")[
            0].find_all("th")
        for x in item_table:
            f.write(x.text + "\n")
f.close()
print("Task completed.")
