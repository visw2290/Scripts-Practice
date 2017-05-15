import logging
import os
os.chdir('C:\\adb')
logging.basicConfig(filename = 'logg.txt',filemode = 'w', level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
log.info('Start of the program')

def summin(n):
	sum = 0
	for i in range(1,n+1):
		log.info('Sum is %s and i value is %s' %(sum,i))
		sum = sum + i
		log.info('Sum is %s' %(sum))
	return sum
if __name__ == '__main__':
	print(summin(20))