#1 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
list = []
for number in range(1500,2701):
    if (number % 7 == 0) and (number % 5 == 0):
        list.append(number)
print(list)
print(len(list))

