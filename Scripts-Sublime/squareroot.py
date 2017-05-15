i=1
def chsqrt(n):
	global i
	while 1:
	    if sqrt(i) == n:
		    print('Square root of n is',i)
		    break
	    elif sqrt(i) > n:
		    print('%d is not a valid square number' %(n))
		    break
	    else:
		    i += 1
def sqrt(x):
	return x**2
chsqrt(625)