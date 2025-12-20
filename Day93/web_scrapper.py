import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://store.steampowered.com/search/?filter=topsellers"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

games = []

results = soup.find_all("a", class_="search_result_row")

for game in results[:20]:  # 상위 20개만
    title = game.find("span", class_="title")
    price = game.find("div", class_="search_price")
    release = game.find("div", class_="search_released")

    games.append({
        "title": title.text.strip() if title else "N/A",
        "price": price.text.strip().replace("\n", " ") if price else "N/A",
        "release_date": release.text.strip() if release else "N/A",
        "url": game["href"]
    })

df = pd.DataFrame(games)
df.to_csv("steam_top_sellers.csv", index=False, encoding="utf-8-sig")

print("✅ steam_top_sellers.csv 생성 완료")
