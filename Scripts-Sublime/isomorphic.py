def iso(str1,str2):
	if len(str1) != len(str2):
		return 'The given strings are not isomorphic'
	dict1 = {}
	for i,j in zip(str1,str2):
		if dict1.get(i,0) == 0:
			dict1[i] = j
		else:
			dict1[i] != j
			return 'The given strings are not isomorphic'
	return 'The string is isomorphic'

print(iso('abcaa','xyzd'))