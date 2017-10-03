def isprime(n):
    for num in range(2,n//2 +1):
        if n%num == 0:
            return 'Not Prime'
        else:
            continue
    return 'Prime'
def primecount(n):
    num = 2
    l1=[]
    while 1:
        if isprime(num)== 'Prime':
            l1.append(num)
            if len(l1) == n:
               break
            else:
                num += 1
        else:
            num += 1
    yield l1
for number in primecount(1000):
    print(number)