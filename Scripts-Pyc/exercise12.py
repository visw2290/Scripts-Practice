'''String 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
 If the string length is less than 2, return instead of the empty string.'''

string = input('Enter the string: ')
if len(string) < 2:
    print('Empty String')
elif len(string) == 2:
    print(string + string)
elif len(string) > 2:
    print(string[0:2] + string[-2:])
