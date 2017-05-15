import os

os.chdir('C:\\adb')
totalSize = 0
for file in os.listdir():
    if not os.path.isfile(file):
        continue
    totalSize = totalSize + os.path.getsize(file)

print(totalSize)
