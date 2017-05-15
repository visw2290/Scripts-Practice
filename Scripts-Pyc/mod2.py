import mod1

class Cat(mod1.Animal):
    name = 'Kittu'
    age = 7
ex2 = Cat()

if __name__ == '__main__':
    print(ex2.name)
    print(ex2.look)
    print(ex2.size)
    print('__name__ = %s' %(mod1.__name__))
