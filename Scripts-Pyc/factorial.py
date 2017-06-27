'''Factorial of a number using recursion'''

def facrec(n):
    if n==1:
        return n
    else:
        return n*facrec(n-1)
print(facrec(6))


'''factorial of a number without recursion'''
def fact(n):
    sum = 1
    while n > 1:
        sum = sum * n
        n -= 1
    return sum

print(fact(5))