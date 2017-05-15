def gensquares(n):
	for num in range(n):
		yield num**2

gens = gensquares(10)
print(gens)
for i in gens:
	print(i)
next(gens)