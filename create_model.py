import csv
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
import numpy
import numpy as np
from joblib import dump, load
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from joblib import dump,load
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
from sklearn.feature_selection import RFE

def print_vals(p, a):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    total = 0
    total1 = 0
    total0 = 0

    for x in xrange(len(p)):
        if int(p[x]) == 1:
            total1 = total1 + 1
        if int(p[x]) == 0:
            total0 = total0 + 1
        if int(p[x]) == 1 and int(a[x]) == 1:
            tp = tp + 1
            total = total + 1
        if int(p[x]) == 1 and int(a[x]) == 0:
            fp = fp + 1
            total = total + 1
        if int(p[x]) == 0 and int(a[x]) == 0:
            tn = tn + 1
            total = total + 1
        if int(p[x]) == 0 and int(a[x]) == 1:
            fn = fn + 1
            total = total + 1
    try:
        tpv = tp/float(tp+fp)
    except:
        tpv = 0.0
    try:
        tnv = tn/float(tn+fn)
    except:
        fpv = 0.0

    print "TPV: %f" % tpv
    print "TNV: %f" % tnv
    print "Total: %d" % total
    print "TP = %d" % tp
    print "FP = %d" % fp
    print "TN = %d" % tn
    print "FN = %d" % fn
    print "Total number of 1's guessed: %d" % total1
    print "Total number of 0's guessed: %d" % total0
    val = float(tp)/float(tp + fn)
    print "TP/TP+FN = %f" % val

num = 0
test_x = []
train_x = []
test_y = []
train_y = []
with open('Data1.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        if num == 0:
            num = num + 1
            continue
        if num < 1000000:
            train_x.append(row)
        else:
            test_x.append(row)
        num = num + 1

num = 0
with open('Labels1.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        if num == 0:
            num = num + 1
            continue
        if num < 1000000:
            train_y.append(row)
        else:
            test_y.append(row)
        num = num + 1

x_test = pd.DataFrame(data = test_x)
x_train = pd.DataFrame(data = train_x)
y_train = pd.DataFrame(data = train_y)
y_test = pd.DataFrame(data = test_y)
y_train = numpy.ravel(y_train)
y_test = numpy.ravel(y_test)

svmp = SVC(gamma='scale', kernel='poly')
svmg = SVC(gamma='scale', kernel='rbf')
kn = KNeighborsClassifier(n_neighbors=9)
neuro= MLPClassifier(solver='lbfgs')
adaBoost = AdaBoostClassifier()
grad = GradientBoostingClassifier()
lr = LogisticRegression()


#dt = DecisionTreeClassifier(max_depth=19)
rf = RandomForestClassifier(n_estimators=101)
'''
sm = SMOTE()
#km=KMeans(n_clusters=36)
features,labels=sm.fit_sample(x_train, y_train)
'''
#print features
#print labels
#print len(features)
#print len(samples)
#exit(1)
#dump(dt, 'dt_model.joblib')
#t = load("kn_model.joblib")
#print kn.score(x_test, y_test)
'''
svmp.fit(features,labels)
hold = svmp.predict(x_test)
#print hold
print "Poly"
print_vals(hold, y_test)
print "\n\n"

print "Guasian"
svmg.fit(features,labels)
hold=svmg.predict(x_test)
print_vals(hold,y_test)
print "\n\n"
'''
'''
print "K nearest Neighbors"
kn.fit(features,labels)
hold=kn.predict(x_test)
print_vals(hold,y_test)
print "\n\n"

del kn 

print "Neuro Network"
neuro.fit(features,labels)
hold=neuro.predict(x_test)
print_vals(hold,y_test)
print "\n\n"

del neuro
print "adaBoost"
adaBoost.fit(features,labels)
hold=adaBoost.predict(x_test)
print_vals(hold,y_test)
print "\n\n"

del adaBoost
print "Gradient Boost"
grad.fit(features,labels)
hold=grad.predict(x_test)
print_vals(hold,y_test)
print "\n\n"

'''

neuro = rf
values=[]
cnt=Counter()
print len(x_test)
#RFE = RFE(rf)
#rf = load('./rf-SMOTE/rf-Smote.joblib')
#RFE.fit(x_train,y_train)
#hold = RFE.predict(x_test)

#dump(RFE, "RFE-Smote.joblib")
RFE = load("RFE-Smote.joblib")
hold = RFE.predict(x_test)
print_vals(hold,y_test)
print "\n\n"
'''
#rf = load('rf-Smote.joblib')
#dump(neuro, "rf-Smote.joblib")

'''
'''
with open("WoodyG.csv", "wb") as csv_file:
    writer = csv.writer(csv_file)
    for line in hold:
        writer.writerow(line)
with open("WoodyT.csv", "wb") as csv_file:
    writer = csv.writer(csv_file)
    for line in y_test:
        writer.writerow(line)




with open("Info.csv", "wb") as csv_file:
    #writer = csv.writer(csv_file)
    for i in range(len(x_test)):
        x=[]
        for j in range(len(x_test.iloc[i])):
            x.append(x_test.iloc[i][j])
        for elm in x:
        	csv_file.write(str(elm)+",")
        csv_file.write('\n')
'''
'''
importance = rf.feature_importances_
importance = pd.DataFrame(importance, index=x_train.columns, columns=["Importance"])
importance["Std"] = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)
x = range(importance.shape[0])
y = importance.ix[:, 0]
#yerr = importance.ix[:, 1]
plt.bar(x, y, align="center")
#plt.xticks(range(0, 18))
plt.ylim(bottom=0)
#plt.xlim(bottom=0)
plt.xlabel("FEATURE")
plt.ylabel("IMPORTANCE")
#plt.xticks(range(0,36),['1.0','','','','2.0','','','','3.0','','','','4.0','','','','5.0','','','','6.0','','','','7.0','','','','8.0','','','','9.0','','',''], rotation=45)
rcParams.update({'figure.autolayout': True})
#plt.savefig("Pulled-By-Inning.pdf")
font = {'family' : 'normal',
        'size'   : 40}
plt.rc('font', **font)
plt.grid(color='black', linestyle='-', linewidth=.5)
#plt.yaxis.set_label_position("right")
#plt.legend(loc='upper right')
plt.xticks(range(0,35),['1','','','','5','','','','','10','','','','','15','','','','','20','','','','','25','','','','','30','','','','','35',''])


plt.title("RANDOM FOREST FEATURE IMPORTANCE")
figure = plt.gcf() # get current figure
figure.set_size_inches(30, 20)





plt.savefig("FEATURE-IMPORTANCE") 
'''
    

