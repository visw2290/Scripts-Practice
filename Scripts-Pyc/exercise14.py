'''Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.'''

string1 = input('Enter First String: ')
string2 = input('Enter second String: ')
list1 = [string2[0:2] + string1[2:],string1[0:2] + string2[2:]]
string3 = ' '.join(list1)
print(string3)
