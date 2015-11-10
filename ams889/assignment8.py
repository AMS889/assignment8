'''
Created on Nov 8, 2015

@author: ams889
'''
import numpy as np
import matplotlib.pyplot as plt
import sys
from investment import investmentClass
from inputValidation import *

if __name__ == "__main__": 
    while True:
        try:
            positions = raw_input("Please enter a list of the shares to buy in parallel: e.g. [1, 10, 100, 1000] ? \n")
            if positions.lower() == "quit":
                break;
            positionsFormatted=positionValidation(positions)
            positionsList=positionList(positionsFormatted)

            num_trials = raw_input("number of trials ? \n")
            if num_trials.lower() == "quit":
                break;
            num_trials = numTrialValidation(num_trials)
            
            resultsFile = open('results.txt','w')
            
            for position in positionsList:
                dailyReturn=investmentClass(position, num_trials).runTrials()
                meanReturn = np.mean(dailyReturn)
                stdReturn = np.std(dailyReturn)
                resultsFile.write("position " + str(position) + ", mean = "   + str(meanReturn) + ", std = " + str(stdReturn) + "\r\n")
                resultsFile.flush()
                p = plt.figure()
                plt.hist(dailyReturn,100,range=[-1,1])
                p.savefig('histogram_'+str(position).zfill(4)+'_pos.pdf')
                plt.clf()
            resultsFile.close()
            
        except ValueError:
            print 'Incorrect Input\n'
    
        except KeyboardInterrupt:
            break
            print "Program Terminated"
            sys.exit(1)

