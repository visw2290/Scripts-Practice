import re

def regcheck1():
    message = ' These are my phone numbers. 9884381871. My secondary number is 9841522371'
    phoneNumber = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
    object = phoneNumber.findall(message)
    print(object)

def regcheck2():
    message = ' My landline number is 044-2377-6831'
    phoneNumber = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
    object = phoneNumber.search(message)
    print(object.group())

regcheck1()
regcheck2()
