'''
Created on Nov 9, 2015

@author: ams889
'''
import unittest
from inputValidation import *
from investment import *

class Test(unittest.TestCase):

    def testInputs(self):
        #Testing valid inputs
        self.assertEqual(positionValidation("[1, 10, 100]"), ["1", "10", "100"])
        self.assertEqual(positionList(["1", "10", "100"]), [1, 10, 100])
        self.assertEqual(numTrialValidation("10000"), 10000)
        #Testing invalid inputs
        self.assertRaises(TypeError,positionValidation,"10, 100")
        self.assertRaises(ValueError,positionList,["1", "10", "15g"])
        self.assertRaises(ValueError,positionList,["1", "10", "-15"])
        self.assertRaises(ValueError,numTrialValidation,"helloworld")
        self.assertRaises(ValueError,numTrialValidation,"-15")

    
if __name__ == "__main__":
    unittest.main()