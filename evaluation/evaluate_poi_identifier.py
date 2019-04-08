#!/usr/bin/python
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.cross_validation import train_test_split

"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)


### your code goes here 

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print "Accuracy: "+str(accuracy_score(y_test, y_pred))
print "Precision: "+str(precision_score(y_test, y_pred))
print "Recall: "+ str(recall_score(y_test, y_pred))
print y_pred
print y_test
print len(X_test)