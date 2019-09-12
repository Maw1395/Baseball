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

neuro = load('Neuro-Smote.joblib')
print "Neuro Network"
#neuro.fit(features,labels)
#hold=neuro.predict(x_test)
#print_vals(hold,y_test)
print "\n\n"

fig, axes = plt.subplots(6,6)
vmin, vmax=neuro.coefs_[0].min(), neuro.coefs_[0].max()
print vmin
for coef, ax in zip(neuro.coefs_[0].T, axes.ravel()):
    print len(coef)
    ax.matshow(np.array(coef, np.float32), cmap=plt.cm.Spectral, vmin=.5*vmin, vmax=.5*vmax)
    ax.set_xticks(())
    ax.set_yticks(())
plt.show()