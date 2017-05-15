'''Write a Python program to get the smallest number from a list.'''

list1 = [9, 4, 6 ,88, 45, 2]
small = list1[0]
for i in list1:
    if i<small:
        small = i
print(small)