class Student():
    try:
        StuCount = 0
        def __init__(self, name, age, mark1, mark2, mark3):
            self.name = name
            self.age = age
            self.mark1 = mark1
            self.mark2 = mark2
            self.mark3 = mark3
            Student.StuCount += 1
        def total(self):
            self.sum = self.mark1 + self.mark2 + self.mark3
            return self.sum
        def average(self):
            self.avg = self.sum/3
            return self.avg
    except:
        print('Enter correct values to get correct results')
dict1 = {'name': 'shiva', 'age': 25, 'mark1': 89, 'mark2':91, 'mark3':86}
list1 = ['viswa',25, 90, 88,86]
e1 = Student(*list1)
print('The total for student e1 is {}'.format(e1.total()))
print(e1.average())
e2 = Student(**dict1)
print(e2.total())
print(Student.StuCount)