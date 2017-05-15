import sys
import os
os.chdir('C:\\adb')
if len(sys.argv) != 2:
    print('Enter the Filename: ')
    raise SystemExit(1)
f = open(sys.argv[1])
lines = f.readlines()
f.close()
flines = [float(line) for line in lines]

print('the max of two numbers is ' + max(flines))
print('the min of two numbers is' + min(flines))