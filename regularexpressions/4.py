import re

#pattern=re.compile('a') #exact match
#pattern=re.compile('a+')
#pattern=re.compile('a*')
#pattern=re.compile('a?')
#pattern=re.compile('a{3}')
pattern=re.compile('a{4,6}')
input="xyzadefaaabpqraaaaaab"

matchers=pattern.finditer(input)

for match in matchers:
    print(match.start(),'....>',match.end(),'.....>', match.group())

