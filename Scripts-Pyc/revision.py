import random

randNumber = random.randint(1,21)
for chance in range(1,7):
    number = int(input('Enter the number:'))
    if number < randNumber:
        print('The entered number is less than the actual number.')
    elif number > randNumber:
        print('The entered number is greater than actual number')
    elif number == randNumber:
        break
if number == randNumber:
    print('You found out the correct number '+ str(randNumber)+' in '+ str(chance) +' chances')
else:
    print('You lost your chances. The correct number is ' +  str(randNumber))
