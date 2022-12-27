# exercice_9_2.py
# a program that categorizes each mail message by which day of the week the
# commit was done. To do this look for lines that start with “From”, then
# look for the third word and keep a running count of each of the days of
# the week. At the end of the program print out the contents of your
# dictionary (order does not matter).

occurence = dict()

fichier = input('Entrer le nom du fichier :')

try:
    fhand = open(fichier)

except BaseException:
    print('Impossible d\'ouvrir le fichier')
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 3: continue
    day = words[2]

    if day not in occurence:
        occurence[day] = 1
    else:
        occurence[day] += 1

print(occurence)
