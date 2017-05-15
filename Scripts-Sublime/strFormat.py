def sum (*args):
	sum = 0
	for i in args:
		sum += i
	print('sum is {}'.format(sum))
sum(9,10,11,12,13)