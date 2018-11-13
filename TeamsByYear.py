from requests import get
from bs4 import BeautifulSoup, Comment

def Teams():
	for year in range(1980, 2018):
		cont = get("https://www.baseball-reference.com/leagues/MLB/" + str(year) + ".shtml").content
		soup = BeautifulSoup(cont, "lxml")
		TeamTable=soup.find("table",{"class": "sortable stats_table", "id": "teams_standard_batting"} )
		Teams = TeamTable.findAll("th", {"class": "left"})
		TeamsUrls=[]
		for Team in Teams:
			try:
				TeamsUrls.append(Team.find("a").get('href'))
			except:
				continue
		#print TeamsUrls
		return TeamsUrls

def Games():
	teams=Teams()
	for i in teams:
		cont = get("https://www.baseball-reference.com/" + i). content
		soup = BeautifulSoup(cont, "lxml")
		Games = soup.findAll("ul", {"class": "timeline"})
		for j in Games:
			Gamesj = j.findAll("li", {"class" : "result"})
		#print Games

			for game in Gamesj:
				print game.find("a").get('href')
	#break
			
		


def main():
	Games()

if __name__ == "__main__":
	main()

#print Teams