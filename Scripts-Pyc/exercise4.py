'''List 2. Write a Python program to multiplies all the items in a list.'''

list1 = [3,5,6,7,9,12]
mul = 1
for number in range(len(list1)):
    mul = mul * list1[number]
print(mul)