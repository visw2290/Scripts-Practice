class Area():
    def __init__(self,r):
        self.r = r
    def Circle(self):
        return 3.14 * self.r * self.r
    def Square(self, length):
        self.length = length
        return self.length * self.length
    def Author(self):
        self.text = 'THis is a beginner'
        return self.text
class Area1(Area):
    def Circle1(self):
        return 3 * self.r * self.r
if __name__ == '__main__':

    a=Area(5)
    print(a.Circle())
    print(a.Square(4))

    list1 = [a.Circle(),a.Square(4)]
    print(list1)



    a1=Area1(10)
    print(a1.Circle1())
    print(a1.Circle())
    print(a1.Author())

