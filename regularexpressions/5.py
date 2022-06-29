import re

input='Hi this is sachin, my runs are 20000 and my phone no 8383838338 and card no 3438438438438'

output=re.sub('[0-9]+','*******',input)
print(output)