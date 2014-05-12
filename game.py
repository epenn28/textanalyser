#! /usr/bin/env python3

from welcome import welcome

welcome()

from my_pyfreq import frequency

doAgain = "y"
while (doAgain == "y"):
    print("Which file would you like to analyze?")
    userInput = input("Type 'a' for the Star-Spangled Banner, 'b' for Take Me Out to the Ball Game, or 'c' for America the Beautiful\n\n")
    
    if (userInput == 'a'):
        print("The following is the frequency of each word in the document:\n\n")
        length = frequency("SSB.txt")
        print()
        print("The document is {0} words long.".format(length))
        #filename = open('SSB.txt', 'r')
        #contents = filename.read()
        #filename.close()
    elif (userInput == 'b'):
        print("The following is the frequency of each word in the document:\n\n")
        length = frequency("Ballgame.txt")
        print()
        print("The document is {0} words long.".format(length))
        #filename = open('Ballgame.txt', 'r')
        #contents = filename.read()
        #filename.close()
    elif (userInput == 'c'):
        print("The following is the frequency of each word in the document:\n\n") 
        length = frequency("ATB.txt")
        print("The document is {0} words long.".format(length))
        #filename = open('ATB.txt', 'r')
        #contents = filename.read()
        #filename.close()
    else:
        print("\n\n")
        print("Invalid input")

    #print("\n")
    #print(contents)
    
    doAgain = input("\nTry again? ('y' or 'n') ")
    while( doAgain != "y" and doAgain != "n" ):
        doAgain = input("Sorry, that's invalid. Please select either 'y' or 'n' ")

print("\n")
print("Thanks for trying the text analyser!")
print("\n")
