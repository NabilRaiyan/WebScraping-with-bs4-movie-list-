import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")

movies_name = soup.find_all(name="h3", class_="title")
movie_list = [movie.get_text() for movie in movies_name][::-1]

with open("movie_list", mode="w", encoding="UTF-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")


