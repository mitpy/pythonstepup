import re;
input='sss@gmail.com'

pattern=re.compile('(^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$)')

isValid=re.fullmatch(pattern,input)
if isValid:
    print('valid email')
else:
    print('Invalid email')