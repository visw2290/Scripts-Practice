'''dictionary 15 Write a Python program to get the maximum and minimum value in a dictionary.'''
dict = {'a': 10,'b':15, 'c':35,'d':5}
max = 0
min = dict['a']
for i in dict.keys():
    if (max < i):
        max = i
    if i < min:
        min = i
print(max)
print(min)
