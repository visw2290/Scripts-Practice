'''dictionary 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.'''

dict = {}
for num in range(1,16):
    dict.setdefault(num,0)
    dict[num] = num * num
print(dict)
