'''List 7. Write a Python program to remove duplicates from a list'''
list1 = [2,3,2,5,6,7]
list2 =[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
