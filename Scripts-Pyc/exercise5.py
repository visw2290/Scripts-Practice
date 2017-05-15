'''LIST 3. Write a Python program to get the largest number from a list.'''

#def maximum(items):
 #   print(max(items))

#maximum([10,20,30,40])

large = 0
list1 = [2,3,4,5,6,7]
for i in list1:
    if i > large:
        large = i
print(large)
