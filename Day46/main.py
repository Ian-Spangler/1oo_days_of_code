# Creating Spotify Playlist using the Musical Time Machine
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

load_dotenv()

SPOTIFY_CLIENT_ID = os.environ["CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
SPOTIFY_REDIRECT_URL = os.environ["REDIRECT_URL"]
SPOTIFY_USERNAME = os.environ["USERNAME"]

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

bilboard_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

bilboard_response = requests.get(url=f"{BILLBOARD_URL}{date}/", headers=bilboard_header)

bilboard_webpage = bilboard_response.text

soup = BeautifulSoup(bilboard_webpage, "html.parser")

top_list = soup.select("li ul li h3")

music_titles = [item.getText().strip() for item in top_list]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URL,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=SPOTIFY_USERNAME))

user_id = sp.current_user()["id"]

uri_list = []

for music in music_titles:
    uri = sp.search(q=f"track:{music} year:{date.split("-")[0]}", type="track")
    try:
        uri_list.append(uri["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{music} doesn't exist in Spotify. Skipped.")

