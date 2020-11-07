'''
   ProjectName:  Enigma Machine                                                
   ProgramName:  Driver.py                                                 
   Author:       Sean Mathews                                    
   Date:         10/29/2020                                          
   Synopsis:
          This is what will be used to drive the program.

   def main(): This is where most of my processess will be initiated.
   def A():mty
   def A():mty
   def A():mty
   def A():mty
   def A():mty
   def A():mty
   
'''
import FileReader as fr
import getFileNames as gfn
import os # To clear the cmd line screen



def printOutAList(theList, startCt, endCt): #process or procedure to print a list.
    os.system("cls")
    for i in range(startCt, endCt):
        print(theList[i])


def convertAValue(welcome, theList):
    pass


def main():

    returntomain = True
    uinput = ""
    
    os.system("cls")
    fr.readTheFileIn(gfn.getWelcome())
    uinput = input("")

    while returntomain == True:
        os.system("cls")
        fr.readTheFileIn(gfn.getMainMenu())
        returntomain = False
        uinput = input("")
       
        if uinput == "A":
            os.system("cls")
            fr.readTheFileIn(gfn.getInformation())
            print("Press Enter for main menu")
            uinput= input("")
            returntomain = True
            
        elif uinput == "B":
            os.system("cls")
            fr.readTheFileIn(gfn.getEncryption())
            print("Press Enter for main menu")
            uinput= input("")
            returntomain = True
        
        elif uinput == "C":
            os.system("cls")
            fr.readTheFileIn(gfn.getDecryption())
            print("Press Enter for main menu")
            uinput= input("")
            returntomain = True
            
        elif uinput == "Q":
            os.system("cls")
            fr.readTheFileIn(gfn.getGoodbye())
            print("Press Enter to Quit")
            uinput= input("")
            print("Goodbye")



"""
    while fr.readTheFileIn(gfn.getWelcome()):
        input == ("> ")
    if input == "A":
        os.system("cls")
        info = fr.readTheFileIn(gfn.getInformation())
    elif input == "M":
        os.system("cls")
        mm = fr.readTheFileIn(gfn.getMainMenu())
    elif input == "B":
        os.system("cls")
        encrypt = fr.readTheFileIn(gfn.getEncryption())
    elif input == "C":
        os.system("cls")
        decrypt = fr.readTheFileIn(gfn.getDecryption())
    elif input == "Q":
        os.system("cls")
        goodbye = fr.readTheFileIn(gfn.getGoodbye())
        
"""
    #print(menu)
    #printOutAList(menu, 1, len(menu))

#####################
main()
