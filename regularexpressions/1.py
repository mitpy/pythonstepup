import re

pattern=re.compile('ab')

input="xyzabdefabpqrab"

matchers=pattern.finditer(input)

for match in matchers:
    print(match.start(),'....>',match.end(),'.....>', match.group())

