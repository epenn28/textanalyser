#! /usr/bin/env python3

import string
from sys import stdin, stdout

def frequency(filename):
    words = {}
    mywords = wordlist(filename)

    for word in mywords:
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1

    #for key in words:
    #    print("{0} {1}".format(words[key], key))

    sortedList = sorted(words, key=words.get)

    for word in sortedList:
        print("The word {0} occurs {1} times.".format(word, words[word]))

    length = len(sortedList)

    return length
    

def wordlist(filename):
    import string
    punc = string.punctuation
    mywords = []

    f = open(filename,'r')

    for line in f:
        for word in line.split():
            for thing in word:
                word = word.strip(punc)

            mywords.append(word)

    f.close()

    return mywords

"""
if __name__ == '__main__':
    frequency("ATB.txt")
   # for word in sorted(words, key = words.get):
   #     print(word, words[word])
   # print(frequency('SSB.txt'))

"""
