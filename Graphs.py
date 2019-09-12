import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams
from collections import OrderedDict
import numpy
def main():
	v=open('Info.csv')
	InfoItem=csv.reader(v)
	v=open('WoodyT.csv')
	TruthItem=csv.reader(v)
	v=open('WoodyG.csv')
	GuessItem=csv.reader(v)
	GuessArray=[]
	TruthArray=[]
	for item in InfoItem:
		GuessLabel=GuessItem.next()
		GuessLabel.append(item)
		TruthLabel=TruthItem.next()
		TruthLabel.append(item)
		GuessArray.append(GuessLabel)
		TruthArray.append(TruthLabel)
	#print TruthArray
	#print GuessArray
	# [in or out],[strike count, balls count, pitch count, strike/ball, outs, inning, slugging, obp, ops, average slugging, average ops, average obp, runs, hits, walks, strike-outs, home-runs, bases]
	#	      [0		1		2	3	     4     5       6         7    8        9                10            11       12    13    14         15        16        17

	TRUEINNINGS=OrderedDict({})
	GUESSINNINGS=OrderedDict({})
	TrueBallStrike=OrderedDict({})
	GuessBallStrike=OrderedDict({})
	TrueRunsGivenUp=OrderedDict({})
	GuessRunsGivenUp=OrderedDict({})
	TruePitchOut=OrderedDict({})
	GuessPitchOut=OrderedDict({})
	TrueStrikes=OrderedDict({})
	GuessStrikes=OrderedDict({})
	for i in TruthArray:
		inning=str(int(i[1][5])+int(i[1][4])*.1)
		if i[0]=='1': #Pitcher has been pulled
		
			if(inning not in TRUEINNINGS):
				TRUEINNINGS[inning]=1
				TrueBallStrike[inning]=float(i[1][3])
				TrueRunsGivenUp[inning]=int(i[1][12])
				TrueStrikes[inning]=int(i[1][0])
				if i[1][4]=='0':
					i[1][4]=1
				TruePitchOut[inning]=float(float(i[1][2])/(float(i[1][4])*1.0+float(i[1][5])*3))
				if(float(float(i[1][2])/float(i[1][4])*1.0)>100):
					print i[1][2], "pitch count"
					print i[1][4], "out count"
					print inning, ""
					print float(float(i[1][2])/float(i[1][4])*1.0)

			else:
				TRUEINNINGS[inning]+=1
				TrueStrikes[inning]+=int(i[1][0])
				TrueBallStrike[inning]+=float(i[1][3])
				TrueRunsGivenUp[inning]+=int(i[1][12])
				if i[1][4]=='0':
					i[1][4]=1
				TruePitchOut[inning]+=float(float(i[1][2])/(float(i[1][4])*1.0+float(i[1][5])*3))
		'''
		else:
			if(inning not in TrueStrikes):
				TrueStrikes[inning]=None
		'''
	for i in GuessArray:
		inning=str(int(i[1][5])+int(i[1][4])*.1)
		if i[0]=='1': #Pitcher has been pulled
			if(inning not in GUESSINNINGS):
				#if float(float(i[1][2])/(float(i[1][4])*1.0+float(i[1][5])*3))>40:
					#continue
				GUESSINNINGS[inning]=1
				GuessStrikes[inning]=int(i[1][0])
				GuessBallStrike[inning]=float(i[1][3])
				GuessRunsGivenUp[inning]=int(i[1][12])
				if i[1][4]=='0':
					i[1][4]=1
				GuessPitchOut[inning]=float(float(i[1][2])/(float(i[1][4])*1.0+float(i[1][5])*3))
			else:
				GUESSINNINGS[inning]+=1
				GuessStrikes[inning]+=int(i[1][0])
				GuessBallStrike[inning]+=float(i[1][3])
				GuessRunsGivenUp[inning]+=int(i[1][12])
				if i[1][4]=='0':
					i[1][4]=1
				GuessPitchOut[inning]+=float(float(i[1][2])/(float(i[1][4])*1.0+float(i[1][5])*3))
				if inning=='9.0' or inning=='9.1' or inning =='9.2':
					print i[1][2]
		'''
		else:
			if(inning not in GuessStrikes):
				GuessStrikes[inning]=None
		'''
	print GuessStrikes
	#print GUESSINNINGS
	TI=OrderedDict({})
	GI=OrderedDict({})
	TBS=OrderedDict({})
	GBS=OrderedDict({})
	TRGU=OrderedDict({})
	GRGU=OrderedDict({})
	TPO=OrderedDict({})
	GPO=OrderedDict({})
	TS=OrderedDict({})
	GS=OrderedDict({})
	for key in sorted(TRUEINNINGS.keys()):
		TI[key]=TRUEINNINGS[key]
	 	TPO[key]=TruePitchOut[key]/(TRUEINNINGS[key]*1.0)
		TBS[key]=TrueBallStrike[key]/TRUEINNINGS[key]
		TRGU[key]=TrueRunsGivenUp[key]/(TRUEINNINGS[key]*1.0)
		TS[key]=TrueStrikes[key]/(TRUEINNINGS[key]*1.0)
		try:
		 	GI[key]=GUESSINNINGS[key]
		 	GPO[key]=GuessPitchOut[key]/(GUESSINNINGS[key]*1.0)
		 	GBS[key]=GuessBallStrike[key]/GUESSINNINGS[key]
		 	GRGU[key]=GuessRunsGivenUp[key]/(GUESSINNINGS[key]*1.0)
		 	GS[key]=GuessStrikes[key]/(GUESSINNINGS[key]*1.0)
		except:
			print key
			GI[str(key)]=None
			GBS[str(key)]=None
			GRGU[str(key)]=None
			GPO[key]=None
			GS[key]=None
	#print GI
	#print GPO.values()
	inning=range(0,36)
	#print TPO.values()
	c=numpy.random.rand(3,1)
	fig = plt.figure()
	host = fig.add_subplot(111)
	
	host.plot(inning, TS.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="TRUTH")
	host.legend(loc='upper right')
	c=numpy.random.rand(3,1)
	host.plot(inning, GS.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="GUESS")
	plt.xlabel("Inning")
	plt.ylabel("Average Strikes Thrown By Pitcher")
	plt.xticks(inning, ( '1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'), rotation=45)
	plt.title("2007-2017 Number of Pitchers Pulled vs Strike To Ball Ratio")
	rcParams.update({'figure.autolayout': True})
	#plt.savefig("Pulled-By-Inning.pdf")
	font = {'family' : 'normal',
	        'size'   : 22}
	plt.rc('font', **font)
	plt.legend(loc='lower right')
	#plt.ylim(ymin=0)
	figure = plt.gcf() # get current figure
	figure.set_size_inches(30, 20)
	#plt.savefig("Strike-to-Ball")
	plt.savefig("Average-Strikes")
	plt.close()
	exit(1)

	c=numpy.random.rand(3,1)
	fig = plt.figure()
	host = fig.add_subplot(111)
	
	#par1 = host.twinx()
	host.plot(inning, TPO.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="TRUTH")
	host.legend(loc='upper right')
	c=numpy.random.rand(3,1)
	host.plot(inning, GPO.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="GUESS")
	plt.xlabel("Inning")
	plt.ylabel("Average Pitches per out")
	plt.xticks(inning, ( '1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'), rotation=45)
	plt.title("2007-2017 Average Pitches Per Out")
	rcParams.update({'figure.autolayout': True})
	#plt.savefig("Pulled-By-Inning.pdf")
	font = {'family' : 'normal',
	        'size'   : 22}
	plt.rc('font', **font)
	plt.legend(loc='upper left')
	#plt.ylim(ymin=0)
	figure = plt.gcf() # get current figure
	figure.set_size_inches(30, 20)
	plt.savefig("Pitches-Out")

	plt.close()
	c=numpy.random.rand(3,1)
	fig = plt.figure()
	host = fig.add_subplot(111)
	
	#par1 = host.twinx()
	host.plot(inning, TRGU.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="TRUTH")
	host.legend(loc='upper right')
	c=numpy.random.rand(3,1)
	host.plot(inning, GRGU.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="GUESS")
	plt.xlabel("Inning")
	plt.ylabel("Average Runs Given Up")
	plt.xticks(inning, ( '1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'), rotation=45)
	plt.title("2007-2017 Avergage Runs Given Up by Inning Pulled")
	rcParams.update({'figure.autolayout': True})
	#plt.savefig("Pulled-By-Inning.pdf")
	font = {'family' : 'normal',
	        'size'   : 22}
	plt.rc('font', **font)
	plt.legend(loc='upper left')
	#plt.ylim(ymin=0)
	figure = plt.gcf() # get current figure
	figure.set_size_inches(30, 20)
	plt.savefig("Runs-Inning")
	plt.close()

	c=numpy.random.rand(3,1)
	fig = plt.figure()
	host = fig.add_subplot(111)
	
	par1 = host.twinx()
	host.plot(inning, TI.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="TRUTH")
	host.legend(loc='upper right')
	c=numpy.random.rand(3,1)
	par1.plot(inning, GI.values(),color=c, marker='o', markeredgecolor=c, markeredgewidth=3, linewidth=3, label="GUESS")
	plt.xlabel("Inning")
	plt.ylabel("Number of Pitchers Pulled")
	plt.xticks(inning, ( '1.0','1.1','1.2','1.3','2.0','2.1','2.2','2.3','3.0','3.1','3.2','3.3','4.0','4.1','4.2','4.3','5.0','5.1','5.2','5.3','6.0','6.1','6.2','6.3','7.0','7.1','7.2','7.3','8.0','8.1','8.2','8.3','9.0','9.1','9.2','9.3'), rotation=45)
	plt.title("2007-2017 Number of Pitchers Pulled vs Inning")
	rcParams.update({'figure.autolayout': True})
	#plt.savefig("Pulled-By-Inning.pdf")
	font = {'family' : 'normal',
	        'size'   : 22}
	plt.rc('font', **font)
	plt.legend(loc='right')
	#plt.ylim(ymin=0)
	figure = plt.gcf() # get current figure
	figure.set_size_inches(30, 20)
	plt.savefig("When-Pulled")
	plt.close()
	
	

if __name__=='__main__':
	main()
