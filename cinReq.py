from requests import get
from bs4 import BeautifulSoup, Comment

teamdict = {
				"ATL": "AtlantaBraves",
				"NYM": "NewYorkMets"
			}

def batter_info(batter, team_key, cont):
	for x in batter:
		if ord(x) > 126:
			batter = batter.replace(x, "")
		if ord(x) == 10:
			batter = batter.replace(x, " ")
	team = teamdict[team_key]
	team = team + "batting"
	soup = BeautifulSoup(cont, "lxml")

	comment = soup.find(string=lambda text:isinstance(text,Comment) and 'id="'+team+'"' in text)
	soup2 = BeautifulSoup(comment, "lxml")
	table = soup2.find("table",{"id": team} )

	for row in table.findAll("tr"):
		cell = row.findAll("th", {"data-stat": "player"})
		for x in cell:
			try:
				current = str(x).split("shtml\">")[1].split("<")[0]
				if current.replace(" ","") == batter:
						cells4 = row.findAll("td", {"data-stat": "onbase_perc"})
						for i in cells4:
							print str(i).split("\">")[1].split("<")[0]

						cells5 = row.findAll("td", {"data-stat": "slugging_perc"})
						for i in cells5:
							print str(i).split("\">")[1].split("<")[0]

						cells6 = row.findAll("td", {"data-stat": "onbase_plus_slugging"})
						for i in cells6:
							print str(i).split("\">")[1].split("<")[0]

			except:
				pass


cont = get("https://www.baseball-reference.com/boxes/NYN/NYN201704030.shtml").content
soup = BeautifulSoup(cont, "lxml")
comment = soup.find(text=lambda n: isinstance(n, Comment) and 'id="play_by_play"' in n)
soup2 = BeautifulSoup(comment, "lxml")
table = soup2.find("table",{"id": "play_by_play"} )

starting1 = ""     #starting pitcher 1
starting2 = ""     #starting pitcher 2
st1f = 0           #starting pitcher flag 1
st2f = 0           #starting pitcher flag 2
currentp = ""      #current pitcher
currentb = ""	   #current batter
currentbt= ""      #current batting team

p1s = 0            #pitcher 1 strikes
p1b = 0            #balls
p1t = 0            #total

p2s = 0            #pitcher 2 strikes
p2b = 0            #balls
pst = 0            #total


for row in table.findAll("tr"):

	cells1 = row.findAll("td", {"data-stat": "pitcher"})
	for z in cells1:
		hold = str(z).split("pitcher\">")[1].split("<")[0]

		if st1f == 0:
			starting1 = hold
			st1f = 1
		if starting1 != hold and st2f == 0:
			starting2 = hold
			st2f = 1
		if starting1 == hold or starting2 == hold:
			print hold
		else:
			exit()

	cells2 = row.findAll("td", {"data-stat": "outs"})

	for z in cells2:
		out = str(z).split("outs\">")[1].split("<")[0]
		if out == "":
			break
		else:
			print "out:" + out

	cells3 = row.findAll("th", {"data-stat": "inning"})

	for z in cells3:
		inning = str(z).split("\">")[1].split("<")[0]
		if inning == "":
			break
		else:
			print "inning:" + inning

	cells4 = row.findAll("td", {"data-stat": "pitches_pbp"})
	for i in cells4:
		print str(i).split("p\">")[1].split("<spa")[0]


	cells5 = row.findAll("td", {"data-stat": "play_desc"})
	for i in cells5:
		print str(i).split("desc\">")[1].split("<")[0]

	cells6 = row.findAll("td", {"data-stat": "batting_team_id"})
	for i in cells6:
		currentbt = str(i).split("\">")[1].split("<")[0]
		print currentbt

	cells7 = row.findAll("td", {"data-stat": "batter"})
	for i in cells7:
		currentb = str(i).split("\">")[1].split("<")[0]
		batter_info(currentb, currentbt, cont)
