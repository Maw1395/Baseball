from requests import get
from bs4 import BeautifulSoup, Comment
import sqlalchemy as db
def Teams():
	TeamsUrls=[]
	for year in range(1980,1981):
		cont = get("https://www.baseball-reference.com/leagues/MLB/" + str(year) + ".shtml").content
		soup = BeautifulSoup(cont, "lxml")
		TeamTable=soup.find("table",{"class": "sortable stats_table", "id": "teams_standard_batting"} )
		Teams = TeamTable.findAll("th", {"class": "left"})

		for Team in Teams:
			try:
				TeamsUrls.append(Team.find("a").get('href'))
			except:
				continue
			#TODO REMOVE BREAK
			#return TeamsUrls
	return TeamsUrls



def Games():
	teams=Teams()
	TotalGames=[]
	for i in teams:
		cont = get("https://www.baseball-reference.com/" + i). content
		soup = BeautifulSoup(cont, "lxml")
		Games = soup.findAll("ul", {"class": "timeline"})

		for j in Games:
			Gamesj = j.findAll("li", {"class" : "result"})
		#print Games

			for game in Gamesj:
				TotalGames.append(game.find("a").get('href'))
			#TODO REMOVE BREAK
			#return TotalGames
	#break
	return TotalGames

