'''
Created on Nov 9, 2015

@author: ams889
'''
import numpy as np

def test_number(num):
    try: #Returns true if tested value is a number, used for input validation
        float(num)
        return True
    except:
        return False

def positionValidation(positions):
    if (positions[0] != "[" or positions[-1] != "]"):
        raise TypeError("Shares must be supplied in a list with square brackets ('[shares]')")
    positionsStripBracket=positions[1:-1]
    positionsFormatted=positionsStripBracket.replace(' ','').split(',')
    return positionsFormatted
  
def positionList(positionsFormatted):
    positionsList=[]
    for p in range(len(positionsFormatted)):
        if test_number(positionsFormatted[p]) == False :
            raise ValueError("Shares must be entered in numeric format")
        elif int(positionsFormatted[p])<0:
            raise ValueError("Shares must be greater than or equal to zero")
        else: positionsList.append(int(positionsFormatted[p]))
    return positionsList

def numTrialValidation(num_trials):
    if test_number(num_trials) == False:
        raise ValueError("Number of trials number be an integer")
    if int(num_trials)<1:
        raise ValueError("There must be at least 1 trial")
    return int(num_trials)