#Write a program to read through a mail log, build a histogram using a
#dictionary to count how many messages have come from each email address,
#and print the dictionary

#This program records the domain name (instead of the address) where the
#message was sent from instead of who the mail came from (i.e., the whole
#email address). At the end of the program, print out the contents of your
#dictionary.

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
    domain = email[email.find('@')+1:]
    if domain not in occurence :
        occurence[domain] = 1
    else:
        occurence[domain] += 1

# identifier le maximum dans le dictionnaire occurence

largest = None

for courriel in occurence :
    val = int(occurence[courriel])
    if largest is None or val > largest :
        largest = val
        largest_mail = courriel

print('Le domaine ayant le plus de courriels est',largest_mail,':',str(largest))
print(occurence)

