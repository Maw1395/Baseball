from requests import get
from bs4 import BeautifulSoup, Comment

cont = get("https://www.baseball-reference.com/boxes/NYN/NYN201704030.shtml").content
soup = BeautifulSoup(cont, "lxml")
comment = soup.find(text=lambda n: isinstance(n, Comment) and 'id="play_by_play"' in n)
soup2 = BeautifulSoup(comment, "lxml")
table = soup2.find("table",{"id": "play_by_play"} )
for row in table.findAll("tr"):
    cells = row.findAll("td", {"data-stat": "pitches_pbp"})
    for i in cells:
   		print str(i).split("p\">")[1].split("<spa")[0]
