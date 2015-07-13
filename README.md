ECE2524 Final Project- Text Analyser

Project Collaborators - Elliot Penn & Chi-Cheung Cheung

This project has three stored text files, which can be selected individually by the user. The Pyfreq program we wrote earlier in the semester runs through the files and puts the information in a dictionary, which is then sorted. The output is a work in progress, but it displays various information about the file (how many words, the most frequent and least frequently used words, etc).

The Text Analyser is a text interface where pyfreq returns the length of the file, which the user inputs. You can start the game by just running the "./game.py " in this directory. Currently it implements 3 files in the game, but if you copy over your personal .txt file within the directory you can use it as well. You may choose 'a' for the Star-Spangled Banner, 'b' for Take Me Out to the Ball Game, 'c' for America the Beautiful, or 'd' (currently not prompted, sort of a "secret option" for now) for your own text files.

This project takes in user input to select a file to parse over with Pyfreq, storing the data in a dictionary. The program can then output various pieces of information about the file. This program aims to follow various elements of the Unix design philosophy, including but not limited to Silence is Golden, the KISS principle, and the rule of Modularity.

