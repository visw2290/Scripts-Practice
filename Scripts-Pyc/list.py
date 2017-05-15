spam = ['a' , 'b', 'c', 'd', 'e']
eggs = ['1', '2', '3', '4', '5']
cheese = [['hello', 'hi', 'heyya'], ['viswa', 'shiva','ram','kishor']]

print(spam[2])
print(eggs[1:4])
print(spam[:3])
print(eggs[2:])
print(spam[0] + ' is the first letter in alphabets ')
print(cheese[0][2])
print(cheese[1][3])

spam[2] = 'C'
eggs[3:5] = ['5', '6', '7']
print(spam)
print(eggs)
print(spam[-2])
print(cheese[1][-1])


del spam[4]
print(spam)

print(len(spam))
print(spam + eggs)
print(spam * 3)

print(9 in eggs)
print('u' in spam)

#spam.index['Hello']
#spam.append
#spam.insert
#spam.remove
#spam.sort
#spam.sort(reverse = True)
#spam.sort(key = str.lower)