import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
best_movies_page = response.text

soup = BeautifulSoup(best_movies_page, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")


with open("movies.txt", "w", encoding="utf-8") as movie_file:
    for title in reversed(movie_titles):
        movie = title.getText()
        movie_file.write(f"{movie}\n")

