message = ' My landline number is 044-2377-6831'
def numberCheck(number):
    if len(number) != 13:
        return False
    for i in range (0,3):
        if not number[i].isdecimal():
            return False
    if number[3] != '-':
        return False
    for i in range(4,8):
        if not number[i].isdecimal():
            return False
    if number[8] != '-':
        return False
    for i in range (9,13):
        if not number[i].isdecimal():
            return False
    return True

print(numberCheck('044-2377-6831'))

for num in range(len(message)):
    chunk = message[num:num+13]
    if numberCheck(chunk):
        print('The number is found. The number is ' +chunk)
