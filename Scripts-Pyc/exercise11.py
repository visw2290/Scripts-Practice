'''string 2. Write a Python program to count the number of characters (character frequency) in a string.'''
import pprint
myLine = input('Enter the string: ')
myDict = {}
for char in myLine.upper():
    myDict.setdefault(char,0)
    myDict[char] = myDict[char] + 1
pprint.pprint(myDict)