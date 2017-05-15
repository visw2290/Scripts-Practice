# Code in global scope cannot use code in local scope defined in functions

def hello():
    number = 10
    print(number)

number = 5
print(number)

#code in local scope can use global variables

def hello1():
    print(num)

num = 15

#code in one function local scope cannot use variables in another local scope

def hello2():
    vals = 10
    print(vals)

hello()
hello1()
hello2()