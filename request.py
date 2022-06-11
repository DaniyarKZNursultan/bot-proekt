import requests
import json
from bs4 import BeautifulSoup


with open("data/popular_movies.html", encoding="utf-8") as file:
    src = file.read()


    data_dict = []
    count = 0

    movies = []
    soup = BeautifulSoup(src, "lxml")
    for td in soup.find_all("td", attrs={"class": "titleColumn"}):
        spisok = td.find_all("a")
        for movie in spisok:
            movie_a = td.find('a').text
            movies.append(movie_a)


    data = {
        'movie_name': movies
    }
    count += 1

    data_dict.append(data)

    with open('popular_movie.json', 'w', encoding='utf-8') as file:
        json.dump(data_dict, file, indent=4)