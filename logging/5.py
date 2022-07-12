import logging;

logging.basicConfig(
    filename='log5.txt',
    level=logging.DEBUG, 
    filemode='w',
    format='%(asctime)s: %(levelname)s : %(message)s',
    datefmt='%d/%m/%y %I:%M:%S '
    )
print('start')
logging.warning("ss")#30
logging.info('info')
logging.error('sss')#40
logging.critical('333')#50
print('end')
