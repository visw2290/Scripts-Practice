class UserError(Exception):
    pass
class Myerror(UserError):
    pass
a = int(input('Enter a number: '))
try:
    if a < 10:
        raise Myerror
    else:
        print('The number succeeded')
except Myerror:
    print('This is an error created and raised by user')
finally:
    print('The test is successful')
