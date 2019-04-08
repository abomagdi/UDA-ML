#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
for dt in data_dict:
    #print(dt)
    tmp = data_dict[dt]["bonus"]
    tmp2 = data_dict[dt]["salary"]
    if((tmp > 5000000 or tmp2 > 1000000)  and str(tmp).find('NaN') < 0 ):
        print(dt+" "+str(data_dict[dt]["salary"])+" "+str(data_dict[dt]["bonus"]))
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

