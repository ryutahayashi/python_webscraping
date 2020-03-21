import urllib.request
from bs4 import BeautifulSoup

#r = requests.get("https://news.yahoo.co.jp/")
url = "https://news.yahoo.co.jp/"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
soup = BeautifulSoup(data, "html.parser")

# pull news topic lists
topics = soup.find("ul", "topicsList_main").text
topic = topics.split(" ")
for title in topic:
    print(title)
