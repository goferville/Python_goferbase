import re
#The match() function only checks if the RE matches
# at the beginning of the string while search() will
# scan forward through the string for a match.

s="A kangroo or gofer567 is a 23.34 x 21.23 Kangroo not " \
  "32.2 0  10 a bba or abba. I am koala123"
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

#find all words
p2=re.compile('\s[a-zA-Z]+\s', re.IGNORECASE)
matches=p2.findall(s)
print('find all words with space at ends:')
for match in matches:
    print(match)
#optional letter
s="color Aug 23, 2018, 's' Jun 01, 2019, 'aa' koala color color colour ,sec sec color"
#here u is optional
p2=re.compile('colou?r', re.IGNORECASE)
matches=p2.findall(s)
print('?=optional :')
for match in matches:
    print(match)
#regex = r"(\w+) (?'day'\d+), (\d{4})"
# same as above
#match group and anmed group
regex = re.compile('(\w+) (?P<day>\d+), (\d{4})', re.IGNORECASE)
match = re.search(regex, "June 24, 2018,")
if match:

    #print("Match at index :", match.start(), match.end())
    # So this will print "June 24"
    print("Full match: ", (match.group(0)))
    # So this will print "June"
    print("Month:",(match.group(1)))
    # So this will print "24"
    print("Day: ",(match.group(2)))
    # So this will print "2018"
    print("Day: ", (match.group(3)))
    print("named:",match.group("day"))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")

#urls
#find all words
s='http://www.intel.commm/ is the web site!'
p2=re.compile(r'^(https?|ftp|file)://\w{3}\.\w+\.[a-zA-Z]{2,5}/?', re.IGNORECASE)
match=p2.search(s)
print(s)
if match:
    print("url: ", match.group(0))

#split string
s='This is ... a test, short and sweet, of split().'
p2=re.compile(r'\W+')
print(p2.split(s))

#Greedy versus Non-Greedy¶
s = '<html><head><title>Title</title>'
p=re.compile(r'<.*>')
match=p.match(s)
if match:
    print(match.group())
s = '<html><head><title>Title</title>'
p=re.compile(r'<.*?>')
match=p.match(s)
if match:
    print(match.group())
p=re.compile(r'<.*?>', re.IGNORECASE)
matches=p.findall(s)
for match in matches:
    print(match)

"""
abc… 	Letters
123… 	Digits
\d 	Any Digit
\D 	Any Non-digit character
. 	Any Character
\. 	Period
[abc] 	Only a, b, or c
[^abc] 	Not a, b, nor c
[a-z] 	Characters a to z
[0-9] 	Numbers 0 to 9
\w 	Any Alphanumeric character
\W 	Any Non-alphanumeric character
{m} 	m Repetitions
{m,n} 	m to n Repetitions
* 	Zero or more repetitions
+ 	One or more repetitions
? 	Optional character, 0 or 1 preceding char
\s 	Any Whitespace
\S 	Any Non-whitespace character
^…$ 	Starts and ends
(…) 	Capture Group
(a(bc)) 	Capture Sub-group
(.*) 	Capture all
(abc|def) 	Matches abc or def	
"""
