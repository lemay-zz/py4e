#Exercise 1: Write a simple program to simulate the operation of the grep
#command on Unix. Ask the user to enter a regular expression and count
#the number of lines that matched the regular expression:

import re
fhand = input ('Like grep : exercice_11.1.py -e \"your regular expression\" -f \"the_file\": ')

try :
    if len(fhand) < 1 :
       fichier = 'mbox-short.txt'

    else:
       fichier = open(fhand)

except :
    print('Enter a valid regular expression!')
    exit()

print(fichier)


