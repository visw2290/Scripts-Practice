try:
    num1 = int(input())
    num2 = int(input())
    num3 = num1 + num2
    print(num3)
except ValueError:
    print('Give correct values')
finally:
    print('All done')

