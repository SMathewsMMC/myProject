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
import Welcome
import MainMenu
import Information
import Encryption
import Decrpytion
import os # To clear the cmd line screen


def printOutAList(theList, startCt, endCt): #process or procedure to print a list.
    os.system("cls")
    for i in range(startCt, endCt):
        print(theList[i])


def convertAValue(menu, theList):
    pass


def main():
    welcome = fr.readTheFileIn(gfn.getWelcome())
    mm = fr.readTheFileIn(gfn.getMainMenu())
    info = fr.readTheFileIn(gfn.getInformation())
    encrypt = fr.readTheFileIn(gfn.getEncryption())
    decrypt = fr.readTheFileIn(gfn.getDecryption())
    os.system("cls")
    input(welcome)
    os.system("cls")
    input(mm)
    os.system("cls")
    input(info)
    os.system("cls")
    input(encrypt)
    os.system("cls")
    input(decrypt)

    #print(menu)
    #printOutAList(menu, 1, len(menu))

#####################
main()
