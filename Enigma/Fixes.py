'''
   ProjectName:  How_Do_I_Do_A_Program                                                
   ProgramName:  Fixes.py                                                 
   Author:       Sean Mathews                                    
   Date:         10/24/2020                                          
   Synopsis:
          This fixes some of the issues we may run into.

   def crlfR():This removes the carage return line
              feed at the end of a test line.
   def A():mty
   def A():mty
   def A():mty
   def A():mty
   def A():mty
   def A():mty
   
'''

def crlfR(theList):
    for i in range(len(theList)):
        theList[i] = theList[i].replace('\n', '')
    return theList
