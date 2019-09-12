import csv
import pandas as pd
import numpy
import numpy as np
from joblib import dump, load
import matplotlib.pyplot as plt
from joblib import dump,load
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

def model(ax, title, inning, secondTitle):
	ax.set_xlabel("\n\n\n\nINNING")
	ax.set_zlabel("\n\n"+title)
	ax.set_xticks(range(0,36))
	ax.set_xticklabels(['1.0','','','','2.0','','','','3.0','','','','4.0','','','','5.0','','','','6.0','','','','7.0','','','','8.0','','','','9.0','','',''], rotation=90)
	#ax.set_xticklabels(['1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'], rotation=90)
	ax.set_ylabel("\n\n\n\n"+secondTitle)
	ax.legend(loc='upper left')

num=0
test_x=[]
truth=[]
guess=[]
with open('Info.csv', 'rb') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		if num == 0:
			num = num + 1
			continue
		test_x.append(row)
		num = num + 1
num=0
with open('WoodyT.csv', 'rb') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		if num == 0:
			num = num + 1
			continue
		truth.append(row)
		num = num + 1
with open('WoodyG.csv', 'rb') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		if num == 0:
			num = num + 1
			continue
		guess.append(row)
		num = num + 1
x_test = pd.DataFrame(data = test_x)
truth =pd.DataFrame(data=truth)
guess=pd.DataFrame(data=guess)
print len(x_test[0]), len(truth[0]),len(guess[0])
#print guess[0]
#print truth[0]



cnt=Counter()
cnt1=Counter()
for i in range(len(x_test[0])):
	#ATTRIBUTE IS DONE HERE
	cnt[x_test[35][i]+":"+x_test[5][i]+":"+x_test[4][i]+':'+truth[0][i]]+=1
	cnt1[x_test[35][i]+":"+x_test[5][i]+":"+x_test[4][i]+':'+guess[0][i]]+=1
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
#ax1=fig.add_subplot(2,1,2,projection='3d')
count=0
for i in cnt:
	inning=i.split(':')[1]
	outs=i.split(':')[2]
	strikes=i.split(':')[0]
	pitchers=cnt[i]
	detT=i.split(':')[3]
	position=(int(inning)-1)*4+int(outs)
	if detT=='1':
		if count==0:
			ax.scatter(position, pitchers, int(strikes),color='b', marker='^', s=60, label='TRUTH')
			count+=1
		else:
			ax.scatter(position, pitchers, int(strikes),color='b', marker='^', s=60)
	model(ax, "NUMBER OF BATTERS FACED", position, "Number of Pitchers Pulled")
count=0
for i in cnt1:
	inning=i.split(':')[1]
	outs=i.split(':')[2]
	strikes=i.split(':')[0]
	pitchers=cnt[i]
	position=(int(inning)-1)*4+int(outs)
	detG=i.split(':')[3]
	if detG=='1':
		if count==0:
			ax.scatter(position, pitchers, int(strikes),color='r', marker='^', s=60,label='GUESS')
			count+=1
		else:
			ax.scatter(position, pitchers, int(strikes),color='r', marker='^', s=60)
	model(ax, "NUMBER OF BATTERS FACED", position, "NUMBER OF PITCHERS PULLED")
	#model(ax1, "Number of Batters Faced", position, "Guess Number of Pitchers Pulled")
ax.legend()
ax.set_ylim(0)
ax.set_xlim(0)
ax.set_zlim(0)
#ax1.set_ylim(0)
#ax1.set_xlim(0)
#ax1.set_zlim(0)
#ax1.view_init(elev=30, azim=165)
ax.view_init(elev=15,azim=145)
#figure = plt.gcf() # get current figure
#figure.set_size_inches(40, 40)
#plt.savefig('Strikes-3d')
#plt.close()
font = {'family' : 'Latin Modern Mono Caps',
        'size'   : 40}	
plt.rc('font', **font)

#plt.rcParams['font.family']='Latin Modern Mono Caps'
#plt.rcParams['font.size']=42
#plt.rcParams.update()


plt.show()
