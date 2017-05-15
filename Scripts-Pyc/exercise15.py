'''string  8. Write a Python function that takes a list of words and returns the length of the longest one.'''

word = input('Enter string values:\n')
list1 = word.split(' ')
length = 0
for i in list1:
    if length<len(i):
        length = len(i)
print(length)