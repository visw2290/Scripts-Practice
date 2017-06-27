'''
Algorithm:
1. Check both the string are equal in length or not. If not then return false
(not Isomorphiic).
2. Create a Generic Dictionary of Key/value pair Character type.
3. Think of first string as array of keys and corresponding each item of this
   array there will be a value in string 2.
4. Check item of str1 exists in dictionary or not as key. If not exists then insert
   a new item (key: str1[i], value: str2[i])
5. If item exists then check for the value of current key, if it doesn't match with
   str2[i] that means strings are not Isomorphic, return false.
'''


def iso(str1,str2):
	dict1={}
	if len(str1) != len(str2):
		return 'Not Iso'
	else:
		for i,j in zip(str1,str2):
			if dict1.get(i,0)==0:
				dict1[i] = j
			elif dict1[i]!=j:
				return 'Not Iso'
	return 'Is Iso'
print(iso('aab','xxy'))