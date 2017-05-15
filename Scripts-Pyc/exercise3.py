'''List: 1. Write a Python program to sum all the items in a list.'''

list1 = [16, 18, 20, 41, 59]
sum = 0
for number in range (len(list1)):
    sum = sum + list1[number]
print(sum)
