'''Sum of natural numbers using recursion'''
def sumN(n):
    if n == 0:
        return n
    else:
        return n+sumN(n-1)

print(sumN(10))

'''Sum of natural numbers without recursion'''

def sumnumber(n):
    sum = 0
    while n >=1:
        sum = sum + n
        n -= 1
    return sum
print(sumnumber(10))