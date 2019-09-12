from requests import get
from bs4 import BeautifulSoup, Comment
import sqlalchemy as db
#GLOBAL TABLE SETUP
engine = db.create_engine('sqlite:////home/woody/Documents/DataMining/Baseball/project.db')
connection = engine.connect()
metadata = db.MetaData()
PlateAppearance = db.Table('PlateAppearance', metadata, autoload=True, autoload_with=engine)

'''
PlateAppearance = db.Table('PlateAppearance', metadata, autoload=True, autoload_with=engine)
TODO REINITALIZE DATABASE
'''
sqlite_file = 'project.db'
table_name = 'PlateAppearance'
#GLOBAL NAME DICT
teamdict = {
				"ATL": "AtlantaBraves",
				"NYM": "NewYorkMets",
				"NYY": "NewYorkYankees",
				"BOS": "BostonRedSox",
				"ARI": "ArizonaDiamondbacks",
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
				"TBD":"TampaBayDevilRays",
				"WSN": "WashingtonNationals"
			}
#ASTROS CHANGE TO AL IN 2013
#BREWERS CHANGE TO NL IN 2013
LeagueDict = {
				"ATL": "NL",
				"NYN": "NL",
				"NYA": "AL",
				"BOS": "AL",
				"ARI": "NL",
				"BAL": "AL",
				"CHN": "NL",
				"CHA": "AL",
				"CIN": "NL",
				"CLE": "AL",
				"COL": "NL",
				"DET": "AL",
				"FLO": "NL",
				"HOU": "NL",
				"KCN": "AL",
				"LAD": "NL",
				"LAN":"AL",
				"MIL": "AL",
				"MIN": "AL",
				"OAK": "AL",
				"PHI": "NL",
				"PIT": "NL",
				"SDN" : "NL",
				"SFN" : "NL",
				"SEA": "AL",
				"SLN": "NL",
				"TBR" : "AL",
				"TBA":"NL",
				"TEX": "AL",
				"TOR": "AL",
				"WAS": "NL",
				"MIA": "NL",
				"MON":"NL",
				"CAL":"AL",
				"ANA":"AL",
				"KCA":"AL",
				"TBD":"AL",
				"WSN": "NL",
				"WAS":"NL"
			}
def Teams():
	TeamsUrls=[]
	for year in range(2007,2018):
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
			#return TotalGames
	#break
	return list(set(TotalGames))
	#This allows for a nonduplicative version of games



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
		try:
			comment = soup.find(string=lambda text:isinstance(text,Comment) and 'id="'+"LosAngelesAngels"+'"' in text)
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
	GamesList = Games()[]
	print 
	PitcherGameNumber={}

	#TODO CHANGE THIS BACK TO ZERO
	#print GamesList
	#GameNumber=2331, 2330, 2329, 7451,7452, 8025,
	GameNumber=0
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
		currPitcherYear=Game.split("/")[3][3:7]
		HomeStadium=Game.split("/")[2]
		
		AwayRecord=str(soup.findAll("div",{"class":"score"})[0].find_next_sibling('div')).split(">")[1].split("<")[0]
		AwayWins=int(AwayRecord.split("-")[0])
		AwayLosses=int(AwayRecord.split("-")[1])
		AwayGameNumber=AwayLosses+AwayWins

		HomeRecord=str(soup.findAll("div",{"class":"score"})[1].find_next_sibling('div')).split(">")[1].split("<")[0]

		HomeWins=int(HomeRecord.split("-")[0])
		HomeLosses=int(HomeRecord.split("-")[1])
		HomeGameNumber=HomeLosses+HomeWins

		HomeTeam=str(soup.find("ul",{ "class": "in_list"}).findAll('li')[1]).split('/')[2]
		AwayTeam=str(soup.find("ul",{ "class": "in_list"}).findAll('li')[1]).split('/')[2]
		



		for row in table.findAll("tr"):
			try:
				inning = str(row.find("th", {"data-stat": "inning"})).split("\">")[1].split("<")[0]
			except:
				continue
				
			#print inning

			if (not inning or inning=="Inn" or (inning[0]!='t' and inning[0]!='b')):
				continue
			

			currPitcher = str(row.find("td", {"data-stat": "pitcher"})).split("pitcher\">")[1].split("<")[0].replace("\xc2\xa0", " ")


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

			if st1f == 0:
					starting1 = currPitcher
					currPitcherYear1=currPitcherYear+starting1
					if currPitcherYear1 not in PitcherGameNumber:
						PitcherGameNumber[currPitcherYear1]=1
					else:
						PitcherGameNumber[currPitcherYear1]+=1
					st1f = 1
			
			if st2f == 0 and not TopofInning:
				starting2 = currPitcher
				currPitcherYear2=currPitcherYear+starting2
				if currPitcherYear2 not in PitcherGameNumber:
					PitcherGameNumber[currPitcherYear2]=1
				else:
					PitcherGameNumber[currPitcherYear2]+=1
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
			PitchSequence=str(row.find("td",{"data-stat":"pitches_pbp"})).split(">")[2].split("<")[0]
			Score=str(row.find("td",{"data-stat":"score_batting_team"})).split(">")[1].split("<")[0]
			opposingScore=int(Score.split("-")[0])
			friendlyScore=int(Score.split("-")[1])
			#return


			# data-stat="batting_team_id">
			'''
			+  following pickoff throw by the catcher
		    *  indicates the following pitch was blocked by the catcher
		    .  marker for play not involving the batter
		    1  pickoff throw to first
		    2  pickoff throw to second
		    3  pickoff throw to third
		    >  Indicates a runner going on the pitch

		    B  ball
		    C  called strike
		    F  foul
		    H  hit batter
		    I  intentional ball
		    K  strike (unknown type)
		    L  foul bunt
		    M  missed bunt attempt
		    N  no pitch (on balks and interference calls)
		    O  foul tip on bunt
		    P  pitchout
		    Q  swinging on pitchout
		    R  foul ball on pitchout
		    S  swinging strike
		    T  foul tip
		    U  unknown or missed pitch
		    V  called ball because pitcher went to his mouth
		    X  ball put into play by batter
		    Y  ball put into play on pitchout
		    '''
			contact=0
			for i in PitchSequence:
					if i =="L" or i =="O" or i =="R" or i =="T" or i=="X" or i =="Y" or i =="F":
						contact+=1
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

			NextBatter=row.find_next_sibling("tr")
			
			while(1):
				try:
					str(NextBatter.find("td", {"data-stat": "batting_team_id"})).split("\">")[1].split("<")[0]
					if NextBatter is None:
							break
					break
				except:
					if NextBatter is None:
							break
					NextBatter=NextBatter.find_next_sibling("tr")
			#print NextBatter.find_next_sibling("tr")
			
			if NextBatter is not None:
				while NextBatter is not None and currentbt!=str(NextBatter.find("td", {"data-stat": "batting_team_id"})).split("\">")[1].split("<")[0]:
					NextBatter=NextBatter.find_next_sibling("tr")
					while(1):
						try:
							if NextBatter is None:
								break
							str(NextBatter.find("td", {"data-stat": "batting_team_id"})).split("\">")[1].split("<")[0]
							break
						except:
							NextBatter=NextBatter.find_next_sibling("tr")

			
			nextbatterstats=[]
			if NextBatter is None:
				nextbatterstats=[0,0,0]
			else:
				nextb=str(NextBatter.find("td", {"data-stat": "batter"})).split("\">")[1].split("<")[0]
				nextbatterstats=batter_info(nextb, currentbt, soup)
			#print batterstats
			#print nextbatterstats
			
			if YEAR>2012 and HomeStadium=="HOU":
				LeagueDict[HomeStadium]="AL"
			if YEAR<2013 and HomeStadium=="HOU":
				LeagueDict[HomeStadium]="NL"
			if YEAR>2012 and HomeStadium=="MIL":
				LeagueDict[HomeStadium]="AL"
			if YEAR<2013 and HomeStadium=="MIL":
				LeagueDict[HomeStadium]="NL"
			

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

				connection.execute(PlateAppearance.insert().values(Team=currentbt,
				Year = YEAR,
				Game_Number = GameNumber,
				Batter_Number = BatterNumberHome,
				Pitcher= currPitcher,
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
				Outcome=playDesc,
				Home_Or_Away=0,
				Batter_Contact=contact,
				Pitcher_Game_Number=999,
				Team_Losses=HomeLosses,
				Team_Wins=HomeWins,
				Team_Game_Number=HomeGameNumber,
				Next_Slugging=nextbatterstats[0],
				Next_Obp=nextbatterstats[1],
				Next_Ops=nextbatterstats[2],
				Home_Stadium=HomeStadium,
				Home_Park_League=LeagueDict[HomeStadium],
				Team_Name=HomeTeam,
				Opposing_Score=opposingScore,
				Friendly_Score=friendlyScore))


				
			else:
				connection.execute(PlateAppearance.insert().values(Team= currentbt,
				Year = YEAR,
				Game_Number = GameNumber,
				Batter_Number =BatterNumberAway,
				Pitcher= currPitcher,
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
				Outcome=playDesc,
				Home_Or_Away=1,
				Batter_Contact=contact,
				Pitcher_Game_Number=999,
				Team_Losses=AwayLosses,
				Team_Wins=AwayWins,
				Team_Game_Number=AwayGameNumber,
				Next_Slugging=nextbatterstats[0],
				Next_Obp=nextbatterstats[1],
				Next_Ops=nextbatterstats[2],
				Home_Stadium=HomeStadium,
				Home_Park_League=LeagueDict[HomeStadium],
				Team_Name=AwayTeam,
				Opposing_Score=opposingScore,
				Friendly_Score=friendlyScore))	
		print GameNumber		
		GameNumber+=1
		#return

				#exit(1)
def main():



	Pitcher_info()
if __name__ == "__main__":
	main()
