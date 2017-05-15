def summ(number):
	sum = 0
	for i in range(number + 1):
		sum = sum + i
	return sum
def mull(number):
	mul = 1
	for i in range(1,number + 1):
		mul = mul * i
	return mul
if __name__ == '__main__':
	print('the sum of n number is {}'.format(summ(20)))
	print('the product of n numbers are {}'.format(mull(10)))