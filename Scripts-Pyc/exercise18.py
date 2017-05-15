'''string 11. Write a Python program to remove the characters which have odd index values of a given string.'''

string = input('Enter the string: ')
word = ''
for sample in string[0::2]:
    word = word + sample
print(word)
