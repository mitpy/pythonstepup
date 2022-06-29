#character classes

import re


#pattern=re.compile('\s')
#pattern=re.compile('\S')
#pattern=re.compile('\d')
#pattern=re.compile('\D')
#pattern=re.compile('\w') 
pattern=re.compile('\W')




input="Hi This is Sachin, my runs are 20000"

matchers=pattern.finditer(input)

for match in matchers:
    print(match.start(),'....>',match.end(),'.....>', match.group())

