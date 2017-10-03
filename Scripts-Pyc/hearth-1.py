a,b = map(int,input().split())
l1 = list(map(int,input().split()))
new_list = []
for count in range(b):
    q1,q2 = map(int,input().split())
    left = q1-1
    right = q2-1
    sum = 0
    total = (q2-q1)+1
    for val in range(left,right+1):
        sum += l1[val]
    new_list.append(sum//total)
for res in new_list:
    print(res)