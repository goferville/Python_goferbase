import re
s="A kangroo or gofer567 is a 23.34 x 21.23 Kangroo not 32.2 0  10 a bba or abba. I am koala123"
p=re.compile('ab', re.IGNORECASE)
#4 or 4 digits (with '.')
p=re.compile('[0-9.]{4,5}')
#3 letter words

#match=p.search(s)
matches=p.findall(s)
print('find 3 or 4 digit number including . :')
for match in matches:
    print(match)

p1=re.compile('kangroo', re.IGNORECASE)
matches=p1.findall(s)
for match in matches:
    print('find word kangroo:')
    print(match)
p2=re.compile('\w{3}', re.IGNORECASE)
matches=p2.findall(s)
print('find any 3 letters:')
for match in matches:
    print(match)

p2=re.compile('\s\w{5}\s', re.IGNORECASE)
matches=p2.findall(s)
print('find any 3 letters with space at ends:')
for match in matches:
    print(match)

p2=re.compile('\w{5}\d{3}', re.IGNORECASE)
matches=p2.findall(s)
print('find any 5 letters + 3 digits:')
for match in matches:
    print(match)
