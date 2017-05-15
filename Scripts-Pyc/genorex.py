import random
def gener(low,high,n):
    for i in range(n):
        rand = random.randint(low, high)
        yield rand
gene = gener(1,5,9)
for i in gene:
    print(i)
gennn = gener(5,18,5)
print(next(gennn))


