def primeI(lower,upper):
    for num in range(lower,upper+1):
        for n in range(2,num):
            if num % n == 0:
                break
        else:
            print(num)

print(primeI(1,100))