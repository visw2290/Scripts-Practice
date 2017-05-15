import random

def viswa(number):
    if number == 1:
        return 'You are first'
    elif number == 2:
        return 'You are second'
    elif number == 3:
        return 'You are third'
    elif number == 4:
        return 'You are fourth'

print('enter a number for the result')
print(viswa(random.randint(1,4))) #randint module imports from random and select any random number from 1 to 4


def check(number):
    return number + 1

myNumber = check(3)
print('The returned number is '+ str(myNumber))
