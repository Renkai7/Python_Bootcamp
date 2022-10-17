from bs4 import BeautifulSoup
import requests

# Get a website page
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(class_="titleline")
article_text = article_tag.getText()
article_link = soup.select_one(selector=".titleline a").get("href")
article_upvote = soup.find(class_="score").getText()



# Get all Article titles, links, and upvote count
articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for anchor in articles:
    text = anchor.getText()
    link = anchor.find("a").get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

# Find article with highest upvote
highest_upvote_position = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote_position], article_upvotes[highest_upvote_position])