'''string 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
 except the first char itself.'''

myLine = input('Enter the string: ')
myLine1 = myLine[0]
myLine = myLine.replace(myLine1,'$')
print(myLine1 + myLine[1:])
