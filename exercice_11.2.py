# Write a program to look for lines of the form: New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

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

total = 0
count = 0
for line in fichier:
    if re.search('New Revision:', line):
        number = re.findall('New Revision: ([0-9]+)', line)
        total = int(number[0]) + total
        count += 1

print('The average is ', int(total/count))
