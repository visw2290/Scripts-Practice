import os
import store
i = 0
print('How many IP addresses do you want to enter?')
ip = int(input())
while i < ip:
    try:
        IpFile1 = open('C:\\aaa\\IPAddress.txt', 'r')
        IpFile = open('C:\\aaa\\IPAddress.txt', 'a')
        list1 = IpFile1.readlines()
        print('Enter the name of the device')
        name = input()
        assert name.isalnum(),'Name should be in alphanumeric format'
        print('Enter the IP Address')
        address = input()
        if (name+'-->'+address+'\n') in list1:
            print('Details already exists')
            continue
        else:
            IpFile.write(name + '-->' + address + '\n')
            i += 1
            list1 = IpFile1.readlines()
    finally:
        IpFile1.close()
        IpFile.close()
print('Thank You for entering IP details')
print(list1)