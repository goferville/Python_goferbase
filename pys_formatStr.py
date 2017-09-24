
lang_info =  [('Fortran', 1954, 0.435), ('Cobol', 1959, 0.391),
              ('C', 1972, 16.076), ('C++', 1980, 9.014),
              ('Python', 1991, 6.482),
              ('Java', 1995, 17.99), ('C#', 2001, 6.687)]
print("{0:12} {1:16} {2:16}".format("Language", "Year Developed",
                                     "TIOBE rating"))
print("-"*46)
for element in lang_info:
    print("{0:12} {1:16} {2:16}".format(element[0], element[1],
                                       element[2]))
"""
'^' -  for center alignment
'<' -  for left alignment 
'>' -  for right alignment
"""
print("{0:12} {1:16} {2:16}".format("Language", "Year Developed",
                                    "TIOBE rating"))
print("-"*46)
for element in lang_info:
    print("{0:12} {1:<16} {2:16}".format(element[0], element[1],
                                         element[2]))
# center alignment
print("{0:<12} {1:^16} {2:>16}".format("Language", "Year Developed",
                                    "TIOBE rating"))
print("-"*46)
for element in lang_info:
    print("{0:12} {1:^16} {2:16}".format(element[0], element[1],
                                         element[2]))
# precision & type flag
print("{0:<12} {1:^16} {2:>16}".format("Language", "Year Developed",
                                    "TIOBE rating"))
print("-"*46)
for element in lang_info:
    print("{0:12} {1:^16} {2:16.3f}".format(element[0], element[1],
                                         element[2]))

# Another example using value n for the type flag.
import locale

# Setting the locale to US English
#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

print("Number without formatting applied: 65739838")
print("Number with formatting applied: {0:n}".format(65739838))