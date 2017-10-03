def primeI(lower,upper):
    for num in range(lower,upper+1):
        for n in range(2,num//2):
            if num % n == 0:
                break
            else:
                print(num)
                break

print(primeI(1,100))