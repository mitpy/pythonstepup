import logging;

logging.basicConfig(filename="log.txt")
print('start')
logging.warning("ss")#30
logging.info("ss")#20
logging.error('sss')#40
logging.critical('333')#50
print('end')
