import sqlalchemy as db
import numpy
import collections
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams

engine = db.create_engine('sqlite:///../project.db')
connection = engine.connect()
metadata = db.MetaData()
PlateAppearance = db.Table('PlateAppearance', metadata, autoload=True, autoload_with=engine)

INNINGS={}
stmt = "select Game_Number, Pitcher, outs, max(inning), outcome from PlateAppearance group by game_number, pitcher, batter_number"
Pitcher = (connection.execute(stmt).fetchall())
game=Pitcher[0][0]
startingPitcher=Pitcher[0][1]
inning=[]
for i in Pitcher:
	if(startingPitcher!=i[1]):
		startingPitcher=i[1]
		inningPlusOuts = max(inning) 
		inning=[]
		if inningPlusOuts not in INNINGS:
			INNINGS[inningPlusOuts]=1
		else:
			INNINGS[inningPlusOuts]+=1	
	thisout=i[2]
	if "Flyball" in i[4] or "out" in i[4]:
		 thisout+=1
	elif "Double Play" in i[4]:
		thisout+=2
	elif "Triple Play" in i[4]:
		thisout+=3
	else:
		thisout=i[2]
	inning.append(i[3]+thisout*.1)
print INNINGS
outlist=[]
for key in sorted(INNINGS.iterkeys()):
     outlist.append(INNINGS[key])
     print key
     
inningslist=range(1000,1036)
c=numpy.random.rand(3,1)
plt.plot(inningslist, outlist,color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3)
plt.xlabel("Inning")
plt.ylabel("Pulled")
plt.xticks(inningslist, ( '1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.2', '2.3', '3.0', '3.1', '3.2', '3.3', '4.0', '4.1', '4.2', '4.3', '5.0', '5.1', '5.2', '5.3', '6.0', '6.1', '6.2', '6.3', '7.0', '7.1', '7.2', '7.3', '8.0', '8.1', '8.2', '8.3', '9.0', '9.1', '9.2', '9.3'))
plt.title("2000-2009 Number of Pitchers Pulled vs Inning and Outs")
rcParams.update({'figure.autolayout': True})
#plt.savefig("Pulled-By-Inning.pdf")
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
plt.rc('font', **font)

plt.show()
