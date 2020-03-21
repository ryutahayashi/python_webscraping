import urllib.request
from bs4 import BeautifulSoup

# yahoo news headline
url = "https://news.yahoo.co.jp/"
# changed it to urllib.request from Requests
uh = urllib.request.urlopen(url)
data = uh.read().decode()
soup = BeautifulSoup(data, "html.parser")

# pull news topic lists
topics = soup.find("ul", "topicsList_main").text
topic = topics.split(" ")
for title in topic:
    print(title)
