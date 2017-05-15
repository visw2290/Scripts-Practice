items = ['vis','shi', 30, 50.8, 90,100.5,'bob']
total = 0
def sum(list):
	total = 0
	for i in list:
		if isinstance(i, int) or isinstance(i,float):
			total += i
	return total
def count(list):
	total = 0
	for i in list:
		if isinstance(i,int) or isinstance(i,float):
			total += 1
	return total
def avg(list):
	sum_items = sum(list)
	noitems = count(list)
	average = sum_items/(noitems * 1.0)
	return average

print(sum(items))
print(count(items))
print(avg(items))