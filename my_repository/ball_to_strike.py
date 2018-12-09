import sqlalchemy as db
import sys
import collections
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams
import numpy

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
for i in Pitcher:
	if(startingPitcher!=i[1]):
		startingPitcher=i[1]
		inningPlusOuts = max(inning) 
		inning=[]
		if inningPlusOuts not in INNINGS:
			INNINGS[inningPlusOuts]=1
			RUNS[inningPlusOuts]=(pitches-balls)/(balls*1.0)
			if balls==0:
				balls=1
		else:
			INNINGS[inningPlusOuts]+=1	
			if balls==0:
				balls=1
			RUNS[inningPlusOuts]+=(pitches-balls)/(balls*1.0)
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
	balls+=i[6]
	pitches+=i[5]
	inning.append(i[3]+thisout*.1)
print INNINGS
outlist=[]
runlist=[]
for key in sorted(INNINGS.iterkeys()):
     outlist.append(INNINGS[key])
     runlist.append(RUNS[key])
     print key
averageScore=[]
for key in range(len(runlist)):
	averageScore.append(runlist[key]/(outlist[key]*1.0))
print averageScore
     
inningslist=range(1000,1036)
c=numpy.random.rand(3,1)
plt.plot(inningslist, averageScore,color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3)
plt.xlabel("Inning")
plt.ylabel("Average Strike to Ball Ratio")
plt.xticks(inningslist, ( '1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.2', '2.3', '3.0', '3.1', '3.2', '3.3', '4.0', '4.1', '4.2', '4.3', '5.0', '5.1', '5.2', '5.3', '6.0', '6.1', '6.2', '6.3', '7.0', '7.1', '7.2', '7.3', '8.0', '8.1', '8.2', '8.3', '9.0', '9.1', '9.2', '9.3'),  rotation=45)
plt.title("2000-2009 Pitchers Pulled By Inning vs Average Ball to Strike Ratio")
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
plt.rc('font', **font)
#plt.savefig("Pulled-By-Inning.pdf")
plt.show()
