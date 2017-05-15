def isprime(n):
	for num in range(2,n):
		if n%num == 0:
			return "Not Prime"
		else:
			continue
	return "Prime"
def Primecount(n):
	number = 2
	count = 0
	while 1:
		if isprime(number) == 'Prime':
			print(number)
			count += 1
			if count == n:
				break
			else:
				number += 1
				continue
		else:
			number += 1
Primecount(40)
