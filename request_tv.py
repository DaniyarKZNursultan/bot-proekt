import requests
import json
from bs4 import BeautifulSoup


with open("data/popular_tv.html", encoding="utf-8") as file:
    src = file.read()


    data_dict = []
    count = 0

    tvs = []
    soup = BeautifulSoup(src, "lxml")
    for td in soup.find_all("td", attrs={"class": "titleColumn"}):
        spisok = td.find_all("a")
        for tv in spisok:
            tv_a = td.find('a').text
            tvs.append(tv_a)
    #for td in soup.find_all("td", attrs={"class": "imdbRating"}):
    #    spisok1 = td.find_all("strong")
    #    for tv1 in spisok1:
    #        tv_str = td.find('strong').text
    #        tvs.append(tv_a + tv_str)


    data = {
        'tv_name': tvs
    }
    count += 1

    data_dict.append(data)

    with open('popular_tv.json', 'w', encoding='utf-8') as file:
        json.dump(data_dict, file, indent=4)