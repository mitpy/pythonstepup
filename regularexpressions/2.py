#character classes

import re

#pattern=re.compile('[abc]')
#pattern=re.compile('[^abc]')
#pattern=re.compile('[a-z]')
#pattern=re.compile('[a-zA-Z]')
#pattern=re.compile('[0-9]')
#pattern=re.compile('[a-zA-Z0-9]')
pattern=re.compile('[^a-zA-Z0-9]')


input="xyzaA*Bb3#33defab3@33pqXYrab123"

matchers=pattern.finditer(input)

for match in matchers:
    print(match.start(),'....>',match.end(),'.....>', match.group())

