import random
print('Hi, Whats your name?')
name = input()
print('Hi! ' + name + ',I have guessed a number from 1 to 20. Try finding the number')
secret = random.randint(1,20)
for guesstaken in range(1,7):
    guessedNumber = int(input())
    if guessedNumber > 20:
        print('Enter a number between 1 to 20 only. You have lost one chance')
    elif guessedNumber > secret:
        print('The number you have guessed is high')
    elif guessedNumber < secret:
        print('The number you have guessed is low')
    else:
        break

if guessedNumber == secret:
    print('Good job ' + name + '. You guessed the right number in ' + str(guesstaken) + ' attempts')
else:
    print('You have failed. The correct guess is ' + str(secret))
