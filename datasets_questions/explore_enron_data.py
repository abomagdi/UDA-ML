#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data['METTS MARK'])

POICounter = 0
SalaryCounter = 0
emailCounter = 0
totalPaymentCounter = 0
poiTotalPaymentNaNCounter = 0
for key in enron_data:
    if(enron_data[key]["salary"] != 'NaN'):
        SalaryCounter +=1
    if(enron_data[key]["email_address"] != 'NaN'):
        emailCounter +=1
    if(enron_data[key]["poi"] == 1):
        POICounter+= 1
    if(enron_data[key]["total_payments"] == 'NaN'):
        totalPaymentCounter+= 1
    if(enron_data[key]["total_payments"] == 'NaN' and enron_data[key]["poi"] == 1):
        poiTotalPaymentNaNCounter+= 1
        

print str(POICounter)
print str(SalaryCounter)
print str(emailCounter)
print str(float(totalPaymentCounter))
print str(float(poiTotalPaymentNaNCounter))

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
