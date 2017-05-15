dict1 = {'name' : 'viswa', 'age':25}
def sum (*args):
	sum = 0
	for i in args:
		sum += i
	print('sum is {}'.format(sum))
def kwgs(**kwargs):
	for i, j in kwargs.items():
		print('Key is {} and value is {}'.format(i,j))
def kwgs1(name, age):
	studentName = name
	studentAge = age
	print('His name is {} aged {}'.format(name,age))
sum(9,10,11,12,13)
kwgs(**dict1)
kwgs1(**dict1)