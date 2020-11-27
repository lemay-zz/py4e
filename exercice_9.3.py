#Write a program to read through a mail log, build a histogram using a
#dictionary to count how many messages have come from each email address,
#and print the dictionary


occurence = dict()

fichier = input('Entrer un nom de fichier : ')

try:
    fhand = open(fichier)

except :
    print('Entrer un nom de fichier valide svp!')
    exit()

for line in fhand :
    mots = line.split()
    if len(mots) < 2 or mots[0] != 'From' : continue
    email = mots[1]
    if email not in occurence :
        occurence[email] = 1
    else:
        occurence[email] += 1

print(occurence)
