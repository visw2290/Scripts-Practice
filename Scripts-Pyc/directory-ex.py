import copy
import pprint

spam = {'name' : 'viswa', 'age': 26, 'sex': 'Male'}
print(spam['name'] + ' is aged ' + str(spam['age']))

print(spam.values())
print(spam.keys())
print(spam.items())
a = spam.get('Address', 'A')
print(a)
spam.setdefault('address', 'adsadsad')
pprint.pprint(spam.items())

def counting():
    myLine = '''Remote purple lays claim to stem,
beside routine stripes of green and brown.
Dark as a patch of shade
in the marsh across the path
that the neighborhood kids and I,
were forbidden to pass. It is
that hue that overtakes,
the marsh that sucks in boots
and offers up skunk cabbage and cattails.
Nests here and overhead.  Who named this plant—
also called bog onion, brown dragon, Indian turnip, wake robin,
Arisaema triphyllum—
and who told me I cannot name. But
his purple—all shadow, all remote and not-remote,
all question marks,
craving. Yes?
This herbaceous perennial, growing from corm
vertical and swollen as it is underground.
Even in late summer, it is not nothing, William
(or Jack),
turning from purple to red before his scattering.'''
    myDict = {}
    for char in myLine.upper():
        myDict.setdefault(char,0)
        myDict[char] = myDict[char] + 1


    pprint.pprint(myDict)

counting()
