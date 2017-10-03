'''Check if the given number is Armstrong number or not
1634 = 1^4 + 6^4 + 3^4 +4^4'''
def Arm(n):
    length = len(str(n))
    num = n
    sum = 0
    while num > 0:
        temp = num % 10
        sum += temp ** length
        num = num//10
    if sum == n:
        return 'Number is Armstrong number'
    else:
        return 'Number is not Armstrong'

print(Arm(1542))