import logging
import os
os.chdir('c:\\adb')
logging.basicConfig(filename = 'log.txt',level = logging.DEBUG,format = '%(asctime)s - %(levelname)s - %(message)s')
def factorial(n):
    logging.debug('Start of the program')
    total = 1
    for i in range(1,n + 1):
        total = total * i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('End of Program')
    return total

print(factorial(8))
