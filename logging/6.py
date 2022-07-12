import logging
from statistics import mode
logging.basicConfig(
    filename='log6.txt', 
    level=logging.DEBUG,
    filemode='a',
    format='%(asctime)s: %(levelname)s : %(message)s',
    datefmt='%d/%m/%y %I:%M:%S '
    )
try:
    x=int(input('first no'))
    y=int(input('second no'))
    print('The result is', x/y)
except ZeroDivisionError as msg:
    print(msg)
    logging.exception(msg)
except ValueError as msg:
    print(msg)
    logging.exception(msg)
    logging.info('execution completed')