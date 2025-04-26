# Creating Spotify Playlist using the Musical Time Machine
from bs4 import BeautifulSoup
import requests

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

bilboard_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


response = requests.get(url=f"{BILLBOARD_URL}{date}/", headers=bilboard_header)

bilboard_webpage = response.text

soup = BeautifulSoup(bilboard_webpage, "html.parser")

top_list = soup.select("li ul li h3")

music_titles = [item.getText().strip() for item in top_list]
