from requests import get
from bs4 import BeautifulSoup, Comment
import sqlalchemy as db
#GLOBAL TABLE SETUP
engine = db.create_engine('sqlite:///project.db')
connection = engine.connect()
metadata = db.MetaData()
PlateAppearance = db.Table('PlateAppearance', metadata, autoload=True, autoload_with=engine)
sqlite_file = 'project.db'
table_name = 'PlateAppearance'
#GLOBAL NAME DICT
teamdict = {
				"ATL": "AtlantaBraves",
				"NYM": "NewYorkMets",
				"NYY": "NewYorkYankees",
				"BOS": "BostonRedSox",
				"ARI": "ArizonaDimondbacks",
				"BAL": "BaltimoreOrioles",
				"CHC": "ChicagoCubs",
				"CHW": "ChicagoWhiteSox",
				"CIN": "CincinnatiReds",
				"CLE": "ClevelandIndians",
				"COL": "ColoradoRockies",
				"DET": "DetroitTigers",
				"FLA": "FloridaMarlins",
				"HOU": "HoustonAstros",
				"KAN": "KansasCityRoyals",
				"LAD": "LosAngelesDodgers",
				"LAA":"LosAngelesAngelsofAnaheim",
				"MIL": "MilwaukeeBrewers",
				"MIN": "MinnesotaTwins",
				"OAK": "OaklandAthletics",
				"PHI": "PhiladelphiaPhillies",
				"PIT": "PittsburghPirates",
				"SDP" : "SanDiegoPadres",
				"SFG" : "SanFranciscoGiants",
				"SEA": "SeattleMariners",
				"STL": "StLouisCardinals",
				"TBR" : "TampaBayRays",
				"TEX": "TexasRangers",
				"TOR": "TorontoBlueJays",
				"WAS": "WashingtonNationals",
				"MIA": "MiamiMarlins",
				"MON":"MontrealExpos",
				"CAL":"CaliforniaAngels",
				"ANA":"AnaheimAngels",
				"KCR":"KansasCityRoyals",
				"TBD":"TampaBayDevilRays"
				"WSN": "WashingtonNationals"


			}
def Teams():
	TeamsUrls=[]
	for year in range(2000,2010):
		#TODO CHANGE THIS BACK TO 2015
		cont = get("https://www.baseball-reference.com/leagues/MLB/" + str(year) + ".shtml").content
		soup = BeautifulSoup(cont, "lxml")
		TeamTable=soup.find("table",{"class": "sortable stats_table", "id": "teams_standard_batting"} )
		Teams = TeamTable.findAll("th", {"class": "left"})

		for Team in Teams:
			try:
				TeamsUrls.append(Team.find("a").get('href'))
			except:
				continue
			
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
	return list(set(TotalGames))



def batter_info(batter, team_key, soup):
	batterStats=[]
	for x in batter:
		if ord(x) > 126:
			batter = batter.replace(x, "")
		if ord(x) == 10:
			batter = batter.replace(x, " ")
	try:
		team = teamdict[team_key]
	except:
		#print team_key
		print team_key
		return batterStats.append(999,999,999)
	team = team + "batting"
	#soup = BeautifulSoup(cont, "lxml")
	try:
		comment = soup.find(string=lambda text:isinstance(text,Comment) and 'id="'+team+'"' in text)
		soup2 = BeautifulSoup(comment, "lxml")
	except:
		return [999,999,999]
	table = soup2.find("table",{"id": team} )
	slg=0.0
	obp=0.0
	ops=0.0
	
	for row in table.findAll("tr"):
		cell = row.find("th", {"data-stat": "player"})
		for x in cell:
			try:
				current = str(x).split("shtml\">")[1].split("<")[0]
				#print row
				if current.replace(" ","") == batter:
					try:
						batterStats.append(float(str(row.find("td", {"data-stat": "onbase_perc"})).split("\">")[1].split("<")[0]))
						batterStats.append(float(str(row.find("td", {"data-stat": "slugging_perc"})).split("\">")[1].split("<")[0]))
						batterStats.append(float(str(row.find("td", {"data-stat": "onbase_plus_slugging"})).split("\">")[1].split("<")[0]))
						if None in batterStats:
							return[999,999,999]
						return batterStats
					except:
						return [999,999,999]
			except:
				continue
def Pitcher_info():
	GamesList = Games()
	GameNumber=0

	#TODO CHANGE THIS BACK TO ZERO
	#print GamesList
	for Game in GamesList:
		#cont = get("https://www.baseball-reference.com/boxes/SFN/SFN201804282.shtml").content
		cont = get("https://www.baseball-reference.com"+Game).content
		YEAR = int(Game.split('/')[3][3:7])
		try:
			soup = BeautifulSoup(cont, "lxml")
			comment = soup.find(text=lambda n: isinstance(n, Comment) and 'id="play_by_play"' in n)
			soup2 = BeautifulSoup(comment, "lxml")
			table = soup2.find("table",{"id": "play_by_play"} )
		except: 
			GameNumber+=1
			continue

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
		hold1 = ''
		hold2 = ''
		BatterNumberHome=0
		BatterNumberAway=0
		BNH=False
		BNA=False
		TopofInning=False
		rep1=False
		rep2=False


		for row in table.findAll("tr"):
			try:
				inning = str(row.find("th", {"data-stat": "inning"})).split("\">")[1].split("<")[0]
			except:
				continue
			#print inning

			if (not inning or inning=="Inn" or (inning[0]!='t' and inning[0]!='b')):
				continue

			currPitcher = str(row.find("td", {"data-stat": "pitcher"})).split("pitcher\">")[1].split("<")[0]

			if inning[0]=='b' or inning[0]=='B':
				TopofInning=False
				BatterNumberHome+=1
				BNH=True;BNA=False
				if(currPitcher!=starting2 and st2f!=0):
					rep2=True
			else:
				TopofInning=True
				BatterNumberAway+=1
				BNH=False;BNA=True
				if (currPitcher!=starting1 and st1f!=0):
					rep1=True
			#print row.findAll("td", {"data-stat": "pitcher"})
			if st1f == 0:
					starting1 = currPitcher
					st1f = 1
			if st2f == 0 and not TopofInning:
				starting2 = currPitcher
				st2f = 1

			if (rep1 and rep2):
				break

			if starting1 != currPitcher and starting2 != currPitcher:
				continue

			out = str(row.find("td", {"data-stat": "outs"})).split("outs\">")[1].split("<")[0]
			#print "out:" + out
			pitches = str(row.find("td", {"data-stat": "pitches_pbp"})).split("p\">")[1].split("<spa")[0]
			playDesc = str(row.find("td", {"data-stat": "play_desc"})).split("desc\">")[1].split("<")[0].replace("\xc2\xa0", " ")
			currentbt=str(row.find("td", {"data-stat": "batting_team_id"})).split("\">")[1].split("<")[0]
			currentb = str(row.find("td", {"data-stat": "batter"})).split("\">")[1].split("<")[0]
			runsScored = int(str(row.find("td", {"data-stat": "score_batting_team"})).split(">")[1].split("-")[0])
			#print "nothing"
			bases = str(row.find("td", {"data-stat": "runners_on_bases_pbp"})).split(">")[1].split("<")[0]
			#exit(1)
			#<td class="left " data-stat="score_batting_team">0-0</td>

			#print runsScored
			#exit(1)
			pitchCount=0
			strkes=0
			balls=0
			try:
				#print "pitches" + pitches
				pitchCount = int(pitches.split(",")[0].strip())
				strikes = int(pitches.split("(")[1].split('-')[0].strip())
				balls = int(pitches.split("(")[1].split('-')[1].split(')')[0].strip())
			except:
				#REMEMBER IF 999 DO NOT COUNT
				pitchCount=999
				strikes=999
				balls=999
			batterstats = batter_info(currentb, currentbt, soup)
			'''print YEAR
			print GameNumber
			print BatterNumberHome
			print currPitcher
			print strikes
			print balls
			print pitchCount
			print out
			print inning[1]
			print batterstats[0]
			print batterstats[1]
			print batterstats[2]
			'''

			if (BNH):

				connection.execute(PlateAppearance.insert().values(Team= currentbt,
				Year = YEAR,
				Game_Number = GameNumber,
				Batter_Number = BatterNumberHome,
				Pitcher= currPitcher.replace("\xc2\xa0", " "),
				Strike = strikes,
				Ball= balls,
				Pitches = pitchCount,
				Outs = out,
				Inning = inning[1],
				Slugging = batterstats[0],
				Obp = batterstats[1],
				Ops = batterstats[2],
				Runs=runsScored,
				Bases=bases,
				Outcome=playDesc))
			else:
				connection.execute(PlateAppearance.insert().values(Team= currentbt,
				Year = YEAR,
				Game_Number = GameNumber,
				Batter_Number =BatterNumberAway,
				Pitcher= currPitcher.replace("\xc2\xa0", " "),
				Strike = strikes,
				Ball= balls,
				Pitches = pitchCount,
				Outs = out,
				Inning = inning[1],
				Slugging = batterstats[0],
				Obp = batterstats[1],
				Ops = batterstats[2],
				Runs=runsScored,
				Bases=bases,
				Outcome=playDesc))
		print GameNumber		
		GameNumber+=1

				#exit(1)
def main():



	Pitcher_info()
if __name__ == "__main__":
	main()
