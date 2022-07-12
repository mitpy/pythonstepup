import logging;

logging.basicConfig(level=logging.DEBUG, filemode='w')
print('start')
logging.warning("ss")#30
logging.info('info')
logging.error('sss')#40
logging.critical('333')#50
print('end')
