import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

titles = soup.find_all(name="h3", class_="title")

titles = titles[::-1]

with open("movies.txt", "a") as file:
    for title in titles:
        try:
            file.write(f"{title.getText()}\n")
        except UnicodeEncodeError:
            file.write("Unable to read this moive\n")
