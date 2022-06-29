#user defined Exceptions
class InvalidSalary(Exception):
    def __init__(self,msg):
        self.msg=msg


sal=int(input('Enter Salary'))
try:
    if(sal < 0):
        raise InvalidSalary('Sal should not be -ve')
except InvalidSalary as i:
    print(i)
    print('Exception raised')
    sal=0

print('My Salary is ', sal)