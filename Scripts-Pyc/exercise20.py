'''string 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.'''

string = input('enter a string:')
count = 0
for i in range (len(string)):
    if string[i].isupper():
        count = count + 1
if count >=2:
    string1 = string.upper()
    print(string1)
else:
    print(string)
