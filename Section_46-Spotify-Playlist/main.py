from bs4 import BeautifulSoup
import requests

year_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Get Website page
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year_choice}")
spotify_web_page = response.text

soup = BeautifulSoup(spotify_web_page, "html.parser")
songs = soup.find_all(id="title-of-a-story", class_="c-title")

for song in songs:
    print(song.getText())
