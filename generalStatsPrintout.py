import sqlalchemy as db
import sys
import collections
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams
import numpy
import math

engine = db.create_engine('sqlite:///../project.db')
connection = engine.connect()
metadata = db.MetaData()
PlateAppearance = db.Table('PlateAppearance', metadata, autoload=True, autoload_with=engine)

INNINGS={}
stmt = "select Game_Number, Pitcher, outs, inning, outcome, pitches, ball from PlateAppearance group by game_number, pitcher, batter_number"
Pitcher = (connection.execute(stmt).fetchall())
game=Pitcher[0][0]
startingPitcher=Pitcher[0][1]
inning=[]
RUNS={}
pitches=0
balls=0
FinalOuts=0
FinalInnings=0
FinalPitches=0
FinalStrikes=0
FinalBalls=0
FinalBattersFaced=0
for i in Pitcher:
	if(startingPitcher!=i[1]):
		startingPitcher=i[1]
		inningPlusOuts = inning
		print inningPlusOuts
		inning=[]
		if inningPlusOuts not in INNINGS:
			INNINGS[inningPlusOuts]=1
			k=inningPlusOuts
			FinalOuts=((math.floor(k)-1)*3+math.floor(((k-math.floor(k))*10)))
			FinalInnings=math.floor(k)+(((k-math.floor(k))*.33))
		else:
			j=math.floor(k)+(((k-math.floor(k))*.33))
			FinalInnings+=j
			FinalOuts=((math.floor(k)-1)*3+math.floor(((k-math.floor(k))*10)))
		pitches=0
		balls=0
	thisout=i[2]
	if "Flyball" in i[4] or "out" in i[4]:
		 thisout+=1
	elif "Double Play" in i[4]:
		thisout+=2
	elif "Triple Play" in i[4]:
		thisout+=3
	else:
		thisout=i[2]
	FinalPitches+=i[5]
	FinalBalls+=i[6]
	FinalStrikes+=i[5]-i[6]
	FinalBattersFaced+=1
	pitches+=i[5]
	inning=i[3]+thisout*.1
print "Total Number of Pitches Thrown ", FinalPitches
print "Total Number of Balls ", FinalBalls
print "Total Number of Strikes", FinalStrikes
print "Total Number of Innings Pitched", FinalInnings
print "Total Number of Outs Recorded", FinalOuts
print "Total Number of Batters Faced", FinalBattersFaced

