def checkPrime(number):
    for num in range(2,number):
        if number % num == 0:
            return 'The number ' + str(number) + ' is not prime'
        else:
            continue
    return ' The number ' + str(number) + ' is prime'
if __name__ == '__main__':
    print(checkPrime(5))