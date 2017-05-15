'''Its a program for getting Yes, no, maybe answers'''
list1 = ['Yes', 'No','Maybe']
SampleFile = open('c:\\aaa\\quiz.txt')
QuestionList = SampleFile.readlines()
try:
    for i in QuestionList:
        print(i)
        Answer = input()
        if Answer.title() not in list1:
            print('Only Yes, No and Maybe accepted as answer!!Try again')
            Answer = input()
finally:
    SampleFile.close()
print("Thanks for participating in the survey")