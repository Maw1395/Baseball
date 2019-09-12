import csv
import pandas as pd
import numpy
import numpy as np
from joblib import dump, load
import matplotlib.pyplot as plt
from joblib import dump,load
from collections import Counter, defaultdict
from matplotlib import rcParams
import itertools

def model(ax, title, inning):
	'''
	ax.set_xlabel("Inning")
	ax.set_ylabel(title)
	ax.set_xticks(range(0,36))
	ax.set_xticklabels(['1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'], rotation=45)
	rcParams.update({'figure.autolayout': True})
	#plt.savefig("Pulled-By-Inning.pdf")
	font = {'family' : 'normal',
	        'size'   : 18}
	plt.rc('font', **font)
	ax.legend(loc='upper left')
	'''
	ax.xlabel("Inning")
	ax.ylabel(title)
	ax.xticks(range(0,36),['1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'], rotation=45)
	rcParams.update({'figure.autolayout': True})
	#plt.savefig("Pulled-By-Inning.pdf")
	font = {'family' : 'normal',
	        'size'   : 40}
	plt.rc('font', **font)
	ax.legend(loc='upper left')

num=0
test_x=[]
truth=[]
guess=[]
with open('Data1.csv', 'rb') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		if num == 0:
			num = num + 1
			continue
		test_x.append(row)
		num = num + 1
num=0
with open('Labels1.csv', 'rb') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		if num == 0:
			num = num + 1
			continue
		truth.append(row)
		num = num + 1
'''
with open('WoodyG.csv', 'rb') as csvfile:
	data = csv.reader(csvfile)
	for row in data:
		if num == 0:
			num = num + 1
			continue
		guess.append(row)
		num = num + 1
'''
x_test = pd.DataFrame(data = test_x)
truth =pd.DataFrame(data=truth)
'''
guess=pd.DataFrame(data=guess)



Gcnt=Counter()
cnt1=Counter()
for i in range(len(x_test[0])):
		if guess[0][i]=='1':
			#print x_test[0][i]
			#ATTRIBUTE HERE
			for j in range(int(x_test[35][i])):
				Gcnt[x_test[5][i]+":"+x_test[4][i]]+=1
			#print x_test[5][i]+':'+x_test[4][i]
			cnt1[x_test[5][i]+":"+x_test[4][i]]+=1
for i in Gcnt:
	Gcnt[i]/=float(cnt1[i])
'''
Tcnt=Counter()
cnt1=Counter()
for i in range(len(x_test[0])):
		if truth [0][i]=='1':
			#print x_test[0][i]
			#ATTRIBUTE HERE
			#for j in range(int(x_test[35][i])):
			for j in range(1):
				#print j
				Tcnt[x_test[5][i]+":"+x_test[4][i]]+=1
			cnt1[x_test[5][i]+":"+x_test[4][i]]+=1
'''
for i in Tcnt:
	Tcnt[i]/=float(cnt1[i])

for i in Tcnt:
	if i not in Gcnt:
		Gcnt[i]=None
'''
fig = plt.figure()
#ax = fig.add_subplot(2,1,1)
#ax1=fig.add_subplot(2,1,2)

'''
for i in Gcnt:
	inning=i.split(':')[0]
	outs=i.split(':')[1]
	position=(int(inning)-1)*4+int(outs)
'''
f = plt.figure()
ax = f.add_subplot(111)
ax.yaxis.tick_right()
ax.yaxis.set_ticks_position('both')

values=[(int(i.split(':')[0])-1)*4+int(i.split(':')[1]) for i in Tcnt.keys()]
lists = sorted(itertools.izip(*[values, Tcnt.values()]))
new_x, new_y = list(itertools.izip(*lists))
plt.plot(new_x, new_y ,color='b', marker='^', label="TRUTH", markeredgecolor='b', markeredgewidth=3, linewidth=3)
#ax.plot(np.unique(values), np.poly1d(np.polyfit(values, Tcnt.values(), 1))(np.unique(values)))
'''
values=[(int(i.split(':')[0])-1)*4+int(i.split(':')[1]) for i in Gcnt.keys()]
lists = sorted(itertools.izip(*[values, Gcnt.values()]))
new_x, new_y = list(itertools.izip(*lists))
plt.plot(new_x, new_y ,color='r', marker='^', label="GUESS",  markeredgecolor='r', markeredgewidth=3, linewidth=3)
'''


plt.xlabel("INNING")
plt.ylabel("NUMBER OF PITCHERS PULLED")
plt.xticks(range(0,36),['1.0','','','','2.0','','','','3.0','','','','4.0','','','','5.0','','','','6.0','','','','7.0','','','','8.0','','','','9.0','','',''], rotation=45)
rcParams.update({'figure.autolayout': True})
#plt.savefig("Pulled-By-Inning.pdf")
font = {'family' : 'normal',
        'size'   : 40}
plt.rc('font', **font)
plt.grid(color='black', linestyle='-', linewidth=.5)
#plt.yaxis.set_label_position("right")
plt.legend(loc='upper right')
plt.title("2007-2017 PITCHERS PULLED BY INNING")
figure = plt.gcf() # get current figure
figure.set_size_inches(30, 20)






plt.savefig("PITCHERS-PULLED-BY-INNING")
plt.close()





#fig.plot(values, Gcnt.values(),color='r', marker='^', label="GUESS")

#For Best Fit
'''
for i in Gcnt:
	if Gcnt[i]==None:
		Gcnt[i]=0
ax1.plot(np.unique(values), np.poly1d(np.polyfit(values, Gcnt.values(), 1))(np.unique(values)))
'''
#print len(Tcnt.keys())
#ax=model(ax, "Number of Strikes", values)
#ax1=model(ax1, "Number of Strikes", values)

#ax.set_ylim(0)
#ax.set_xlim(0)

#ax1.set_ylim(0)
#ax1.set_xlim(0)

