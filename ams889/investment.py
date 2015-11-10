'''
Created on Nov 8, 2015

@author: ams889
'''
import numpy as np

class investmentClass(object):
    #Class used to simulate trials on each position invested in
    
    def __init__(self, position, num_trials):
        self.position=int(position)
        self.num_trials=int(num_trials)
        self.position_value = 1000 / self.position
    
    def runTrials(self):
        cumu_ret = []
        daily_ret = []
        for trial in range(self.num_trials):
            gain = np.random.uniform(size=self.position)<=0.51 #the probability of a gain is 51%
            cumu_ret.append(gain.sum()*self.position_value*2) 
            daily_ret.append((cumu_ret[trial]/1000.)-1)
        return daily_ret