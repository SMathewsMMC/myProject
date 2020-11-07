'''
   ProjectName:How_I_Do_A_Program
   Program: FileReader.py
   Author: Ed Cauthorn
   Date: Oct 16, 2020
   Synoposis:
     This process takes a filename and
     then dumps it to a list. 

   def readTheFileIn(fileName): Reads a file into a list.
   defA():mty
   defA():mty
   defA():mty
   defA():mty
   defA():mty
   defA():mty
   defA():mty

'''
#import testing as test
import Fixes as fx
    
def readTheFileIn(fileName):
    fO = open(fileName,"r")
    theList = fO.readlines()
    fO.close()
    theList = fx.crlfR(theList)
    
    for i in range(0, 24):
        #test.writeOutAString(theList[i])
        print(theList[i])

    return theList   

