#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    ### your code goes here
    for i in range(0,90,1):
        currentPred = predictions[i]
        currentAge  = ages[i]
        currentNetWo = net_worths[i]
        error = abs((currentPred - currentNetWo)/currentNetWo)
        if(error < 0.9):
            cleaned_data.append((currentAge,currentNetWo,error))
    
    return cleaned_data

