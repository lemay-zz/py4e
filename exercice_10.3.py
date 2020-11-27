# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input to
# lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z. Find
# text samples from several different languages and see how letter frequency
# varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

import string
lettre = dict()
total = 0
fichier = input('Entrez un nom de fichier : ')
if len(fichier) < 1 :
    fichier = 'mbox-short.txt'

try :
    fhand = open(fichier)

except :
    print('Entrez un nom de fichier valide svp')
    exit()

for line in fhand :
    line = line.strip()
    line = line.lower()
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','',string.digits))
    line = line.replace(' ','').replace('\t','')
    line = list(line)
    if len(line) == 0 : continue

    for letter in line :
        lettre[letter] = lettre.get(letter, 0) +1
        total += 1

lst =list()
for k,v in list(lettre.items()) :
    lst.append((k,v))

lst.sort()
print('nombre de lettres :',total)
for k,v in lst :
    print(k,("{:.1%}".format(v/total)))
