# Exercise 10

# Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json

query=input("Enter What type of news you want: ")

url=f"https://newsapi.org/v2/everything?q={query}&from=2024-06-12&sortBy=publishedAt&apiKey=358c44b45c4c479d852bbdf6a8cae788"        # Url from newapi.org"

r=requests.get(url)

print(r.text)

news=json.loads(r.text)

for article in news["articles"]:
    print(article["source"])
    print(article["title"])
    print(article["description"])
    print("------------------------------")