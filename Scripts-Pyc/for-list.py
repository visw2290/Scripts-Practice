def example():

    myList = ['dog', 'cat', 'fish', 'lion', 'tiger']
    for i in range(len(myList)):
        print('Index ' + str(i) + ' has value ' + myList[i])


def example2():
    myList2 = list(range(0,10))
    for i in range(len(myList2)):
        print(myList2[i])

example()
example2()

