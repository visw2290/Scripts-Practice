class Animal():
    name = 'Blacky'
    size = 'normal'
    look = 'cute'
    @property
    def get_name(self):
        return self.name

ex1 = Animal()

if __name__ == '__main__':
    print(ex1.name)
    print(ex1.get_name)
    print('__name__ = %s' %(__name__))
    print(ex1)