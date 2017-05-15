number = int(input('enter the number: '))
e1 = 0
e2 = 1
for i in range(number):
    temp = e1
    print(temp)
    e3 = e1 + e2
    e1 = e2
    e2 = e3
