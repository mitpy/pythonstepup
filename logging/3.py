import logging;

logging.basicConfig(filename="log3.txt",level=logging.DEBUG, filemode='w')
print('start')
logging.warning("ss")#30
logging.info('info')
logging.error('sss')#40
logging.critical('333')#50
print('end')
