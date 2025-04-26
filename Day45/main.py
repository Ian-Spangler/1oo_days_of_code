from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))
print(article_texts[index])
print(article_links[index])


# import lxml
#
# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml") # For some website, use lxml
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup.prettify())
#
# print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# heading_2 = soup.select(".heading")
# print(heading_2)