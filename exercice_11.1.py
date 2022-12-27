# Exercise 1: Write a simple program to simulate the operation of the grep
# command on Unix. Ask the user to enter a regular expression and count
# the number of lines that matched the regular expression:

import re
fhand = input('Enter a file to search: ')
try:
    if len(fhand) < 1:
        fichier = open('mbox-short.txt', encoding="UTF-8")
    else:
        fichier = open(fhand, encoding="UTF-8")
except BaseException:
    print('Enter a valid file name!')
    exit()

regex = input('Enter a regular expression: ')
occurence = 0
for line in fichier:
    # if I use rstrip() a get a wrong result on mbox.txt with java$
    # grep gives me 4175 but if the next line is uncommented
    # the program gives 4218... why? There is 43 lines ending with
    # java\s (white space after java).
    # line = line.rstrip()
    if re.search(regex, line):
        occurence += 1
print(fhand, 'had', occurence, 'lines that matched', regex)
