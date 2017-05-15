import logg
import logging
logging.basicConfig(filename = 'logg.txt',filemode = 'w', level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
log.info ('The sum of 30 numbers is %s' %(logg.summin(30)))
#print('The product of 5 numbers is %s' %(func.mull(5)))