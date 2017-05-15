import os

fileOpen = open('c:\\BU Chats\example.txt','w')
fileOpen.write('Hey this is my program')
fileOpen.close()

fileOpen = open('c:\\BU Chats\example.txt')
print(fileOpen.read())
print(fileOpen.readlines())
fileOpen.close()

fileOpen = open('c:\\BU Chats\\example.txt', 'a')
fileOpen.write('\nI have changed and appended the program')
fileOpen.close()

fileOpen = open('c:\\BU Chats\\example.txt')
print(fileOpen.read())
print(fileOpen.readlines())
fileOpen.close()

fileOpen =open('c:\\BU Chats\\example.txt')
print(fileOpen.readlines())


