#! /usr/bin/env python3

from welcome import welcome

welcome()

#import pyfreq

doAgain = "y"
while (doAgain == "y"):
    print("Which file would you like to analyze?")
    userInput = input("Type 'a' for the Star-Spangled Banner, 'b' for Take Me Out to the Ball Game, or 'c' for America the Beautiful\n")
    if (userInput == 'a'):
        filename = open('SSB.txt', 'r')
        contents = filename.read()
        filename.close()
    elif (userInput == 'b'):
        filename = open('Ballgame.txt', 'r')
        contents = filename.read()
        filename.close()
    elif (userInput == 'c'):
        filename = open('ATB.txt', 'r')
        contents = filename.read()
        filename.close()
    else:
        contents = "Invalid input"

    print("\n")
    print(contents)
    
    doAgain = input("\nTry again? ('y' or 'n') ")
    while( doAgain != "y" and doAgain != "n" ):
        doAgain = input("Sorry, that's invalid. Please select either 'y' or 'n' ")

print("\n")
print("Thanks for playing!")
print("\n")
